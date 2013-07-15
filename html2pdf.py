#!/usr/bin/python

import os, sys
import subprocess
# import re

# Open a file
path = "/home/jharri34/learnpythonthehardway.org/book"
dirs = os.listdir( path )

# This would print all the files and directories
for file in dirs:
	# subprocess.call('type '+file,shell=True)
	
  	subprocess.call("wkhtmltopdf "+file+" "+str(file).split('.')[0], shell=True)


