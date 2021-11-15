# Binary search
#
# You start in the middle of the list, ...
# then you search the second half.

import os

words = []
file = os.path.dirname(__file__) + "/words.txt"
for line in open(file):
    word = line.strip()
    words.append(word)


def full_search(words, keyword):
    i = 0
    for word in words:
        i = i + 1
        if (word == keyword):
            return i
    return i

def binary_search(words, keyword, i=0):
    i = i + 1
    key = len(words) // 2

    if words[key] == keyword:
        return i
   
    if keyword < words[key]:
        words = words[:key]
    else:
        words = words[key+1:]
    
    i = binary_search(words, keyword, i)
    return i


print("Words: " + str(len(words)))
print("Full search loops: " + str(full_search(words, "mother")))
print("Binary search loops: " + str(binary_search(words, "mother")))
    # Words: 113783
    # Full search loops: 62889
    # Binary search loops: 16
