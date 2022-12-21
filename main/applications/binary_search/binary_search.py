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
   
    if keyword < words[key]: #Look Here
        words = words[:key]
    else:
        words = words[key+1:]
    
    i = binary_search(words, keyword, i)
    return i


print(len(words)) # 113783
print(full_search(words, "mother")) # 62889
print(binary_search(words, "mother")) # 16