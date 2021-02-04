#!/usr/bin/env python3

import os
from pathlib import Path
import datetime

#Create a datetime object
dt = datetime.datetime.now()

#Create a day, month and year attribute
day = dt.day
month = dt.month
year = dt.year

#Change path to where logs will go

os.chdir(Path('/home/jared/projects/programming/net_automation/py_scripts/radius_clear/path_to_test_files'))

#Verify you are in the correct path

print(Path.cwd())

#Create a for loop that generates a file with the date as it's title

#for i in range(1, 32):

    #Create a file for each iteration
    #Remember i must be converted to a string with str()

    #testFile = open('Dec_'+str(i)+'_2020.txt', 'w')

#Create a log with the name based on the day's date

log = open(str(month)+'_'+str(day)+'_'+str(year)+'.txt', 'w')
