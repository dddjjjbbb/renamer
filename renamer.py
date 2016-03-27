#!/usr/bin/env python

'''Rename files in CWD from Dictionary '''

from filenameDictionary import filenamesToConvert
import os
import os.path

path = os.getcwd()
filenames = os.listdir(path)

for filename in filenames:
	if filename in filenamesToConvert:
		os.rename(filename, filenamesToConvert.get(filename))

