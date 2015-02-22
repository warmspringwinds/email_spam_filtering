import numpy
from sklearn.grid_search import GridSearchCV
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.externals import joblib

from custom_sklearn_lib import ( 
                                Contains_HTML_Transformer,
                                Contains_Re_Transformer,
                                Contains_Spam_Transformer,
                                Contains_URL_Transformer,
                                Text_Length_Transformer
                                )

from spam_data import fetch_training_set


def get_best_classifier_using_grid_search(train_data='default'):
    
    if train_data == 'default':
        train_data = fetch_training_set()
    
    parameters = {
        'features__words__vect__min_df': (1, 3, 5),
        'features__words__vect__token_pattern': (r"\b[^\W\d_]+\b",),
        'features__words__vect__binary': (False,),
        'features__words__frequency_transform__use_idf' : (True,),
        'features__words__vect__ngram_range': ((1, 1), (1, 2)),
        'clf__C': (1, 5, 10),
        'clf__kernel': ('linear', 'rbf')
    }
    
    pipeline = Pipeline([
        ('features', FeatureUnion([
            ('words', Pipeline([
                ('vect',  CountVectorizer()),
                ('frequency_transform',  TfidfTransformer())
            ])),
            ('url_feature',  Contains_URL_Transformer()),
            ('html_feature', Contains_HTML_Transformer()),
            ('scaled_length_feature', Pipeline([
                ('length_feature', Text_Length_Transformer()),
                ('frequency_transform',  StandardScaler())
            ])),
            ('spam_feature', Contains_Spam_Transformer()),
            ('response_feature', Contains_Re_Transformer())
            ])),
        ('clf',  SVC())
    ])
    
    train_texts = numpy.asarray(train_data['text'])
    train_texts_class_labels = numpy.asarray(train_data['class'])
    
    grid_search = GridSearchCV(pipeline, parameters, n_jobs=-1, verbose=1)
    
    grid_search.fit(train_texts, train_texts_class_labels)

    best_classifier = {}
    
    best_classifier['classifier'] = grid_search.best_estimator_
    best_classifier['classifier_score'] = grid_search.best_score_
    
    return best_classifier

def save_classifier_into_file(classifier, file_name):
    
    joblib.dump(classifier, file_name)

def load_model_from_file(file_name):
    
    return joblib.load(file_name)
    
def compute_best_classifier_and_save(file_name):
    
    classifier = get_best_classifier_using_grid_search()
    save_classifier_into_file(classifier, file_name)
    