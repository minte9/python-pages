# Histogram
# 
# How many times each letter appears
# The get method takes a key and a default value

def histogram(str):
    dictionary = dict()
    for ch in str:
        if ch not in dictionary:
            dictionary[ch] = 1
        else:
            dictionary[ch] += 1
    return dictionary

assert histogram("google") != {}
assert histogram("google") != {'g': 0, 'o': 0, 'l': 0, 'e': 0}
assert histogram("google") == {'g': 2, 'o': 2, 'l': 1, 'e': 1}


# get(key, default)

assert histogram("yahoo").get('o') == 2
assert histogram("yahoo").get('o', 0) == 2