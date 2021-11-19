# Opening a file in write mode ...
# clears out old data if the files exists.
#
# If the file doesn't exists a new one is created.
#
# The os module provides functions for working with files and directories.

import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file = dir_path + "/data/myfile1.txt"

fp = open(file, "w")
fp.write("New line 1 \n")
fp.write("New line 2 \n")
fp.close()

f = open(file)
print(f.read())
    # New line 1 
    # New line 2 