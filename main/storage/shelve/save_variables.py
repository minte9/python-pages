"""Shelve module:
You can save and restore variables from the hard drive.
New files are generated in working directory:
mydata.bak, mydata.dat
"""
import shelve

file = shelve.open('mydata')
answers =['a', 'b', 'c']
file['answers'] = answers
file.close()