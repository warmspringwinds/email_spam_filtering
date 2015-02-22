import spam_filter

file_name_to_save_classifier_to = 'classifier_dump/classifier.dump'

classifier = get_best_classifier_using_grid_search()

spam_filter.save_classifier_into_file(classifier, file_name_to_save_classifier_to)

print classifier['classifier_score']