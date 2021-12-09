"""CSV reader:
It's not enough to just split the text file by comma.
Maybe files use escape characters to allowed commas as part of values.
Always use csv module for reading and writing CSV files.
The most convenient to access values in the reader object ...
is to convert it to a list
"""
import csv, pathlib
DIR = pathlib.Path(__file__).resolve().parent


"""Convert the csv reader to a list:
"""
with open(DIR / 'data/file1.csv') as file:
    reader = csv.reader(file)
    data = list(reader)
    assert data[0][0] == '11'
    assert data[0][1] == '12'


"""With large files you'll want a for loop:
"""
with open(DIR / 'data/file1.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
            # ['11', '12', '12']
            # ['21', '22', '23']
            # ['31', '32', '33']