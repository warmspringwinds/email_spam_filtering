Welcome to the ADCG SPAM DATASET, which is one of the datasets for 
the data mining competition associated with CSDMC2010 SPAM corpus.

This dataset is composed of a selection of mail messages, suitable for 
use in testing spam filtering systems.  

------------------------------------------------------
Pertinent points

  - All headers are reproduced in full.  Some address obfuscation has taken
    place, and hostnames in some cases have been replaced with
    "csmining.org" (which has a valid MX record) and with most of the recipents
    replaced with 'hibody.csming.org' In most cases
    though, the headers appear as they were received.

  - All of these messages were posted to public fora, were sent to me in the
    knowledge that they may be made public, were sent by me, or originated as
    newsletters from public mail lists. A part of the data is from other 
    public corpus(es), however, for some reason, information will be open
    after the competion.

  - Copyright for the text in the messages remains with the original senders.

------------------------------------------------------
TR-mails.zip FILES contains 2500 mails both in Ham(1721) labelled as 1 and Spam(779) labelled as 0.
TT-mails.zip FILES contains 1827 mails both in Ham and Spam

The file spam-mail.tr.label is the associated training labels.

The GOAL is to classify the testing set for ham/spam.
  
------------------------------------------------------
The email format description
 
The format of the .eml file is definde in RFC822, and information on recent 
standard of email, i.e., MIME (Multipurpose Internet Mail Extensions) can be
find in RFC2045-2049.
 
------------------------------------------------------    
On the provide python script

Since some data mining techniques only make use of the subject and body of the
email to identify spam. In this package, we have included a simple python 
script (ExtractContent.py) which can help to extract the subject and body of the email. 
    
    In a python compatible environment, ( the code is test on python 2.5.1 and should
    work on python 2.x)
    
    1, invoke the script by command 
    ./ExtractContent.py
    2, input source directory -- where you store the source files
    For exmaple
    C:\EMAILPro\CSDMC2010_SPAM\TEST
    3, input destination directory -- where you want the extracted body to be
    For example
    C:\EMAILPro\CSDMC2010_SPAM\TEST_NEW
    4, we are done

Note that, the script only extract limited information from the email (no 
information of fields like to, from, attachment are extract but only the subject
and the first part of the body.) By oferring such a script we just want to show 
a simple preprocessing method where the participants can start from. 
More advanced method which makes use of email header information or even attachment 
information are encouraged.
     
------------------------------------------------------    
Please direct any questions regarding this dataset to xiaohu@in.tum.de

