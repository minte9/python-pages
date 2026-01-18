# --------------------------------------------
# HASHING (DICTIONARY)
# --------------------------------------------
# A hash is a function that takes a value (on any kind) and returns an integer.
# Dictionaries use these integers to store and look up key-value pairs.
#
# Dictionary keys must be hashable.
# Mutable types (like lists) are NOT.

data = {}

data["one"] = 1
data[1] = "abc"

print(data)
# {'one': 1, 1: 'abc'}


# ---------------------------
# Unhasable types (ERROR)

items = [1, 2]
# data[items] = 3

# TypeError: unhashable type: 'list'
# List can change - dictionaries need keys that never change