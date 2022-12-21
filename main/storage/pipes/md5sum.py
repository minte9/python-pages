# Using pipe ...
# you can use md5sum ...
# to check if two files have the same content.

import os

DIR = os.path.dirname(os.path.realpath(__file__))

file1 = DIR + "/data/01.txt"
f = open(file1, "w")
f.write("1234567890")
f.close()

file2 = DIR + "/data/02.txt"
f = open(file2, "w")
f.write("1234567890")
f.close()

def md5sum (filename):
    cmd = 'md5sum ' + filename
    fp = os.popen(cmd)
    res = fp.read() 
    print(res) 
        # 5a92d5b6e2303c7fea60297d2c985713  01.txt
    md5sum = res.replace(filename, '')
    stat = fp.close()
    return md5sum

assert md5sum(file1) == md5sum(file2) # pass
