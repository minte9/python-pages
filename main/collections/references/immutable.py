""" Immutable vs mutable types:
If the object is mutable, changes in one reference affect all names.
If the object is immutable, reasigning create a new object.
"""

# List (mutable)

a = [1, 2, 3]
b = a  # b reference the same list
b.append(4)  # mutating b changes a
print(a)  # [1, 2, 3, 4]

# Dictionary (mutable)

user = {'name': 'Alice', 'age': 25}
profile = user  # profile references the same dict
profile['age'] = 26
print(user)  # {'name': 'Alice', 'age': 26}

# Set (mutable)

fruits = {"apple", "banana"}
basket = fruits  # basket references the same set
basket.add("orange")
print(fruits)  # {'apple', 'banana', 'orange'}


# Integer (immutable)

a = 10
b = a  # b references the same int object (10)
b += 5  # creates a new int object (15) and rebinds b
print(a)  # 10 (unchanged)
print(b)  # 15 

# String (immutable)

a = "hello"
b = a  # b references the same string
b += " world"  # creates a new string object "hello world"
print(a)  # hello (unchanged)
print(b)  # hello world

# Tupple (immutable)

a = (1, 2, 3)
b = a  # b references the same tuple
b += (4,)  # creates a 'new tuple' (1, 2, 3, 4)
print(a)  # (1, 2, 3) - unchanged
print(b)  # (1, 2, 3, 4)