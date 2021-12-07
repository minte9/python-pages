"""Shelve module:
You can save and restore variables from the hard drive.
New binary files are generated in working directory.
Shelves values don't need to be opened in read or write mode,
they can do both, once opened.
"""
import shelve, os

DIR = os.path.dirname(os.path.realpath(__file__))
FILE = DIR + "/data/vars.shelve"

# Open shelf and write a list variable
SH = shelve.open(FILE)
answers = ['a', 'b', 'c']
SH['answers'] = answers
SH.close()

# Open shelf and add a value
SH = shelve.open(FILE)
answers = list(SH['answers'])
answers.append('d') # Look Here
SH['answers'] = answers
SH.close()

# Open shelf and get values
SH = shelve.open(FILE)
answers = SH['answers']
print(answers[3])
SH.close()

# Tests
assert answers[3] == 'd'
assert answers[:3] == ['a', 'b', 'c']