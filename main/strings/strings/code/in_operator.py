""" The `in` is a boolean operator
    Returns True if the fist string appears as a substring in the second one
    The repr() function returns a printable representation of the given object
""" 

import os

file = os.path.dirname(__file__) + "/../data/words.txt"
rows = open(file)

def exists(word):
    for char in word:

        if char == "e":
            return False
            
    return True

W = []  # words
E = []  # word with no e

for row in rows:
    word = row.strip()
    W.append(word)

    if (exists(word)):
        E.append(word)  
    
print("Words: " + repr(len(W)))
print("Words (with char e): " + repr(len(E)))

"""
    Words: 113783
    Words (with char e): 37621
"""