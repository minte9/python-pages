# ------------------------------------
# REFERENCES
# ------------------------------------
# Variables are names bound to objects.
# Assigning one variable to another 
# copies the reference, not the object.
#
# In Python everything is an object.

a = [1, 2, 3]   # a references the list object
b = a           # b references the SAME list object

b.append(4)     # modify the list through b

print(a)  # [1, 2, 3, 4]
print(b)  # [1, 2, 3, 4]

assert a == b   # a and b point to the same list in memory


# ----------------------------------------
# HASH vs REFERENCE
# ----------------------------------------
# There are three different things people often mix up:
# 1. The variable names (a, b)
# 2. The object in memory (the list [1, 2, 3, 4])
# 3. The has of an object (used for dictionary keys)
#
# Variables don't have hashes.
# Only objects can have a hash.
#
# The list object has no hash, because lists are mutable.
# Hashes must never change.


# --------------------------
# IDENTITY
# --------------------------
# Python lets you check the identity using id().
# This proves that a and b point to the same object.

a = [1, 2, 3]
b = a

print(id(a))  # 140103271591744
print(id(b))  # 140103271591744


# -----------------------------
# IMMUTABLE OBJECTS - HASHABLE
# -----------------------------

a = (1, 2, 3)
b = a

print(id(a) == id(b))   # True
print(hash(a))          # OK
print(hash(b))          # Same hash