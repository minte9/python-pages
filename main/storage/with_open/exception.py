"""Using with open statement
you have excellent handling in case of exception."""

import os

DIR = os.path.dirname(os.path.realpath(__file__))
file = DIR + "/data/file.txt"

with open(file, "w") as f:
    f.write("0")

try:
    print("Open file to read ...")
    with open(file) as f:
        data = f.read()
        x = 1 / data # 1 / 0
        print(data) # line not reached
except:
    print("Error!")
    if f.closed == False:
        print("File not closed - not ok")
    else:
        print("File closed before exception - ok")

