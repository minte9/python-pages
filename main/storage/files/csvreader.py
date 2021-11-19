# Write and read csv

import os
import csv

DIR = os.path.dirname(os.path.realpath(__file__))
FILE = DIR + "/data/myfile2.csv"

f = open(FILE, "w")
f.write("c1, c2, c3 \n")
f.write("11, 12, 13 \n")
f.write("12, 22, 23 \n")
f.write("13, 32, 33 \n")
f.close()

f = open(FILE, "r")
assert f.readline().strip() == "c1, c2, c3"
assert f.readline().strip() == "11, 12, 13"


# Walk - Read directories and files

for root, dirs, files in os.walk(DIR + "/data/"):
    for name in files:
        if name.endswith(".csv"):
            path = os.path.join(root, name)
            assert path.endswith(".csv")
            assert name == "myfile2.csv"


# Csv - reader

file = DIR + "/data/myfile2.csv"
data = list(csv.reader(open(file), delimiter=","))
assert data[0] == ['c1', ' c2', ' c3 ']
assert data[1] == ['11', ' 12', ' 13 ']