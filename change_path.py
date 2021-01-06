import os
from pathlib import Path

#Change the pwd to the directory in os.chdir()
#Makes sure that you are putting files in a specific directory

os.chdir(Path('/home/jared/projects/programming/py_scripts/radius_clear/path_to_test_files'))

#Print out the pwd to make sure it is the correct directory

print(Path.cwd())
