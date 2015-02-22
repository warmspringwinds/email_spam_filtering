#!/usr/bin/python
# FileName: Subsampling.py 
# Version 1.0 by Tao Ban, 2010.5.26
# This function extract all the contents, ie subject and first part from the .eml file 
# and store it in a new file with the same name in the dst dir. 

import email.parser 
import os, sys, stat

def ExtractSubPayload (filename):
	''' Extract the subject and payload from the .eml file.
	
	'''
	if not os.path.exists(filename): # dest path doesnot exist
		print "ERROR: input file does not exist:", filename
		os.exit(1)

	fp = open(filename)
	msg = email.message_from_file(fp)

	charset = msg.get_content_charset()

	payload = msg.get_payload(decode=True)

	if type(payload) == type(list()):
		payload = payload[0] # only use the first part of payload
	sub = msg.get('subject')

	print charset
	
	if sub:
		if charset and (charset != 'default'):
			sub = unicode(sub, encoding=charset, errors='ignore')
		else:
			sub = unicode(sub, errors='ignore')
	else:
		sub = u''

	#sub = sub.encode('utf-8')

	if payload:
		#if type(payload) != type(''):
			#payload = str(payload)
		if charset and (charset != 'default'):
			payload = unicode(payload, encoding=charset, errors='ignore')
		else:
			payload = unicode(payload, errors='ignore')
	else:
		payload = u''


	#payload = payload.encode('utf-8')

	return (sub + payload).encode('utf-8')

def ExtractBodyFromDir ( srcdir, dstdir ):
	'''Extract the body information from all .eml files in the srcdir and 
	
	save the file to the dstdir with the same name.'''
	if not os.path.exists(dstdir): # dest path doesnot exist
		os.makedirs(dstdir)  
	files = os.listdir(srcdir)
	for file in files:
		srcpath = os.path.join(srcdir, file)
		dstpath = os.path.join(dstdir, file)
		src_info = os.stat(srcpath)

		print file
		if stat.S_ISDIR(src_info.st_mode): # for subfolders, recurse
			ExtractBodyFromDir(srcpath, dstpath)
		else:  # copy the file
			body = ExtractSubPayload (srcpath)
			dstfile = open(dstpath, 'w')
			dstfile.write(body)
			dstfile.close()

def extract_test_and_train_mail_bodies(srcdir_train, srcdir_test, dstdir_train, dstdir_test):
	
	if not os.path.exists(srcdir_train):
		print 'The source directory %s does not exist, exit...' % (srcdir_train)
		sys.exit()
	
	if not os.path.exists(srcdir_test):
		print 'The source directory %s does not exist, exit...' % (srcdir_test)
		sys.exit()
	
	if not os.path.exists(dstdir_train):
		os.makedirs(dstdir_train)
	
	if not os.path.exists(dstdir_test):
		os.makedirs(dstdir_test)
	
	ExtractBodyFromDir(srcdir_train, dstdir_train)
	ExtractBodyFromDir(srcdir_test, dstdir_test)

###################################################################
# main function start here
# srcdir is the directory where the .eml are stored

# print 'Input source directory: ' #ask for source and dest dirs
# srcdir = raw_input()
# if not os.path.exists(srcdir):
# 	print 'The source directory %s does not exist, exit...' % (srcdir)
# 	sys.exit()
# # dstdir is the directory where the content .eml are stored
# print 'Input destination directory: ' #ask for source and dest dirs
# dstdir = raw_input()
# if not os.path.exists(dstdir):
# 	print 'The destination directory is newly created.'
# 	os.makedirs(dstdir)

###################################################################
# ExtractBodyFromDir ( srcdir, dstdir ) 


