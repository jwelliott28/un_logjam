#!/usr/bin/env python3

import os
from pathlib import Path

os.chdir(Path('/home/jared/projects/programming/py_scripts/radius_clear/path_to_test_files'))

print(Path.cwd())

for i in range(1, 32):

    #Create a file for each iteration
    #Remember i must be converted to a string with str()

    testFile = open('Dec_'+str(i)+'_2020.txt', 'w')

