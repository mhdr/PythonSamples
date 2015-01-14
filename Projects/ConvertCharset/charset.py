#!/usr/bin/python3

# usage : ./charset.py filename


__author__ = 'mahmood'


import codecs
import shutil
import sys
import os

file_name=sys.argv[1]
backup_file_name="{0}.bak".format(file_name)
# create a backup of file first
shutil.copy2(file_name,backup_file_name)
print("backup created for file : {0}".format(backup_file_name))

# read content of file
source_file= codecs.open(file_name,"r","Windows-1256")
contents=source_file.read()
source_file.close()
# remove file to create a new one with utf-8 charset
os.remove(file_name)

# write contents to file with utf-8 charset
target_file=codecs.open(file_name,"w","utf-8")
target_file.write(contents)
target_file.close()

print("{0} successfully converted to utf-8 format".format(file_name))