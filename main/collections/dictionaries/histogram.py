# Histogram
# 
# How many times each letter appears
# To get a value use get(key, default) method
#
# Use for statement to traverse the keys of the dictionaries.
# The keys are in no order.


# string histogram

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


# foreach key, print value

h = histogram("google")
for k in h:
    print(k + ": " + str(h[k]))
        # g: 2
        # o: 2
        # l: 1
        # e: 1


# invert histogram - to map the frequencies to letters

def invert_histogram(d):
    dictionary = dict()
    for key in d:
        value = d[key]
        if value not in dictionary:
            dictionary[value] = [key]  # new row list
        else:
            dictionary[value].append(key)  # add to row list
    return dictionary

h = invert_histogram(histogram("google"))
for k in h:
    print(k, h[k])
        # 2 ['g', 'o']
        # 1 ['l', 'e']