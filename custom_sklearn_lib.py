import re
import numpy
from scipy.sparse import csr_matrix
from sklearn.base import BaseEstimator, TransformerMixin

CONTAINS_URL_REGEX = re.compile(r"http[s]?://")
CONTAINS_HTML_REGEX = re.compile(r"<[^>]+>")
CONTAINS_SPAM_REGEX = re.compile(r"spam", re.IGNORECASE)
RESPONSE_EMAIL_REGEX = re.compile(r"Re:", re.IGNORECASE)

class Contains_URL_Transformer(BaseEstimator, TransformerMixin):
    
    def __init__(self):
        pass
    
    def transform(self, X):
        
        column_amount, = X.shape
        result = csr_matrix((column_amount, 1))
        
        for index, doc in enumerate(X):
            contains_url = CONTAINS_URL_REGEX.search(doc)
            if contains_url is not None:
                result[index, 0] = 1
        
        return result

    def fit(self, X, y=None):
        return self

class Contains_Spam_Transformer(BaseEstimator, TransformerMixin):
    
    def __init__(self):
        pass
    
    def transform(self, X):
        
        column_amount, = X.shape
        result = csr_matrix((column_amount, 1))
        
        for index, doc in enumerate(X):
            contains_url = CONTAINS_SPAM_REGEX.search(doc)
            if contains_url is not None:
                result[index, 0] = 1
        
        return result

    def fit(self, X, y=None):
        return self

class Contains_HTML_Transformer(BaseEstimator, TransformerMixin):
    
    def __init__(self):
        pass
    
    def transform(self, X):
        
        column_amount, = X.shape
        result = csr_matrix((column_amount, 1))
        
        for index, doc in enumerate(X):
            contains_url = CONTAINS_HTML_REGEX.search(doc)
            if contains_url is not None:
                result[index, 0] = 1
        
        return result

    def fit(self, X, y=None):
        return self

class Contains_Re_Transformer(BaseEstimator, TransformerMixin):
    
    def __init__(self):
        pass
    
    def transform(self, X):
        
        column_amount, = X.shape
        result = csr_matrix((column_amount, 1))
        
        for index, doc in enumerate(X):
            contains_url = RESPONSE_EMAIL_REGEX.search(doc)
            if contains_url is not None:
                result[index, 0] = 1
        
        return result

    def fit(self, X, y=None):
        return self

class Text_Length_Transformer(BaseEstimator, TransformerMixin):
    
    def __init__(self):
        pass
    
    def transform(self, X):
        
        column_amount, = X.shape
        result = numpy.ndarray((column_amount, 1))
        
        for index, doc in enumerate(X):
            result[index, 0] = len(doc)
        
        return result

    def fit(self, X, y=None):
        return self
