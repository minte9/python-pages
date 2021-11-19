# Open a file in wrrite mode (default is read)
# 
# The old data is cleared if the files exists.
# If the file doesn't exists a new one is created.
#
# The os module ...
# provides functions for working with files and directories.

import os

DIR = os.path.dirname(os.path.realpath(__file__))
file = DIR + "/data/myfile1.txt"

fp = open(file, "w")
fp.write("New line 1 \n")
fp.write("New line 2 \n")
fp.close()

f = open(file)
print(f.read())
    # New line 1 
    # New line 2 