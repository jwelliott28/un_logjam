#!/usr/bin/env python3

import os
from pathlib import Path
import datetime

#Change path to where you want to store test files
os.chdir(Path('/home/jared/projects/programming/py_scripts/radius_clear/path_to_test_files'))

#Print the cwd to make sure you are in the correct directory
print(Path.cwd())

#Create a variable for the datetime object
dt = datetime.datetime.now()

#Create a variable for day, month and year dt attributes
day = dt.day
month = dt.month
year = dt.year

#Create a file using the date variables and writing it with 'w' option
log = open(str(month)+'_'+str(day)+'_'+str(year)+'.txt', 'w')
