import pandas
import os
from ExtractContent import extract_test_and_train_mail_bodies as _run_extraction

# Folder containing mails' bodies for training with labels
TRAIN_DATA_DIR = 'mails_bodies_train'

# Folder containing mails' bodies for testing without labels
TEST_DATA_DIR = 'mails_bodies_test'

# Table of file number and corresponding class lable (0 - not spam, 1 - spam)
CLASS_LABLES_FILE = 'spam-mail.tr.label'

# Folder containing raw training mails
RAW_TRAIN_MAILS_FOLDER = 'TR'

# Folder containing raw test mails
RAW_TEST_MAILS_FOLDER = 'TT'

def get_not_hidden_filenames_in_directory(directory_name):
    """
    Returns list with filenames of files in @directory_name that don't
    start with '.'. These files are usually supposed to be hidden.
    """
    checking_function = lambda file_name: not file_name.startswith('.')
    
    all_filenames = os.listdir(directory_name)
    result_filenames = filter(checking_function, all_filenames)
    
    return result_filenames

def fetch_training_set():
    """
    Extracts mails' bodies from TRAIN_DATA_DIR module variable.
    Returns pandas.DataFrame with columns 'text' and 'class'.
    'text' - unicode string.
    'class' - int. 0 - spam, 1 - ham.
    Run extract_mails_bodies_from_raw_mails() before using this 
    function to extract pure mail bodies.
    This is the case when you don't have TRAIN_DATA_DIR and TEST_DATA_DIR folders.
    """
    
    train_files_names = get_not_hidden_filenames_in_directory(TRAIN_DATA_DIR)
    class_lables = pandas.read_csv(CLASS_LABLES_FILE)
    
    train_data = pandas.DataFrame({'text': [], 'class': []})
    
    for file_name in train_files_names:
        
        srcpath = os.path.join(TRAIN_DATA_DIR, file_name)
        # Fetch file's id from file's name
        file_number_string = file_name.split('_')[1].split('.')[0]
        file_number = int(file_number_string)
        # Get the class of training sample by id
        # iloc[] - integer indexing. loc[] - lable indexing
        class_number = class_lables[class_lables['Id'] == file_number]['Prediction'].iloc[0]
        # All files are in utf-8
        text = unicode( open(srcpath).read(), encoding='utf-8')
        data_frame = pandas.DataFrame({'text': [text], 'class': [class_number]})
        train_data = train_data.append(data_frame, ignore_index=True)
    
    return train_data

def fetch_test_set():
    """
    Extracts mails' bodies from TEST_DATA_DIR module variable.
    Returns pandas.DataFrame with columns 'text'.
    'text' - unicode string.
    Run extract_mails_bodies_from_raw_mails() before using this 
    function to extract pure mail bodies.
    This is the case when you don't have TRAIN_DATA_DIR and TEST_DATA_DIR folders.
    """
    
    test_files_names = get_not_hidden_filenames_in_directory(TEST_DATA_DIR)
    test_data = pandas.DataFrame({'Id': [], 'text': []})
    
    for file_name in test_files_names:
        
        srcpath = os.path.join(TEST_DATA_DIR, file_name)
        # Fetch file's id from file's name
        file_number_string = file_name.split('_')[1].split('.')[0]
        file_number = int(file_number_string)
        # All files are in utf-8
        text = unicode( open(srcpath).read(), encoding='utf-8')
        data_frame = pandas.DataFrame({'Id': [file_number], 'text': [text]})
        test_data = test_data.append(data_frame, ignore_index=True)
    
    return test_data

def extract_mails_bodies_from_raw_mails():
    """
    Extracts raw mails' bodies to new folders for later use.
    """
    _run_extraction(RAW_TRAIN_MAILS_FOLDER, RAW_TEST_MAILS_FOLDER,
                                        TRAIN_DATA_DIR, TEST_DATA_DIR)