# Dictionary hashes:
#
# A hash is a function that takes a value (on any kind) and returns an integer.
# Dictionaries use these integers to store and look up key-value pairs.
#
# The keys have to be hashable.
# Mutable types like lists are not hashable.

dict = {}
dict["one"] = 1
dict[1] = "abc"

print(dict) # {'one': 1, 1: 'abc'}

list = [1, 2]
# dict[list] = 3
    # TypeError: unhashable type: 'list'