import numpy
import pandas
import spam_filter
import spam_data

classifier = spam_filter.load_model_from_file('classifier_dump/classifier.dump')

classifier_accuracy = classifier['classifier_score']

classifier_obj = classifier['classifier']

test_data = spam_data.fetch_test_set()

result = classifier_obj.predict(numpy.asarray(test_data['text']))

final = pandas.DataFrame({'Id': numpy.asarray(test_data['Id']), 'Prediction': numpy.asarray(result)})

final = final.astype(int)

final = final.sort(['Id'])

final.to_csv('final_1.csv', index=False)



