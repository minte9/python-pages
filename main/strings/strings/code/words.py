# Open file and search through words list
# Return number of words with no e in them

import os

file = os.path.dirname(__file__) + "/../data/words.txt"
rows = open(file)

def has_no_e(word):
    for letter in word:
        if letter == "e":
            return False
    return True

W = [] # words
E = [] # word with no e

for row in rows:
    word = row.strip()
    W.append(word)
    if (has_no_e(word)):
        E.append(word)  
    

print("W: " + repr(len(W)))
print("E: " + repr(len(E)))