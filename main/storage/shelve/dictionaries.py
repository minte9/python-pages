"""Shelve dictionaries:
Like dictionaries, shelf values have keys() and values() methods
"""
import shelve, sys, os

DIR = os.path.dirname(os.path.realpath(__file__))
FILE = DIR + "/data/dict.shelve"
db = shelve.open(FILE)

dict = db['spanish'] if 'spanish' in db.keys() else {}

if len(sys.argv) == 3: # Command line add item
    if sys.argv[1] == 'add':
        words = sys.argv[2].split(':')
        dict[words[0]] = words[1]

db['spanish'] = dict
print(db['spanish'])
db.close()

# dictionaries.py
# {}
#
# dictionaries.py add one:uno
# {'one': 'uno'}
#
# dictionaries.py add one:uno
# {'one': 'uno', 'two': 'dos'}