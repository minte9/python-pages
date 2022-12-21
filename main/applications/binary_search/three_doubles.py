# Get the words with three consecutive double letters

import os

def has_three_doubles(word):
    i = 0
    jj = 0
    while i < len(word) -1:
        if word[i] == word[i+1]:
            jj = jj + 1
            if jj == 3:
                return True
            i = i + 2
        else:
            jj = 0
            i = i + 1
    return False

assert has_three_doubles("aabbcc") == True
assert has_three_doubles("Mississippi") == False

file = os.path.dirname(__file__) + "/words.txt"
for line in open(file):
    word = line.strip()
    if has_three_doubles(word):
        print(word)
        
        # bookkeeper
        # bookkeepers
        # bookkeeping
        # bookkeepings