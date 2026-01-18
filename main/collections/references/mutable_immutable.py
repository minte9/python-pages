# --------------------------------------------
# MUTABLE vs IMMUTABLE
# --------------------------------------------
# Mutable: changes affect all references
# Immutable: reasignment creates a new object


# --------------------------------------------
# MUTABLE Types
# ---------------------------------------------


# LIST
# ----------

a = [1, 2, 3]
b = a               # same list reference

b.append(4)         # modify list reference

print(a)  # [1, 2, 3, 4]
print(b)  # [1, 2, 3, 4]


# DICTIONARY
# ----------

user = {'name': 'Alice', 'age': 25}
profile = user      # same dictionary reference

profile['age'] = 26

print(user)         # {'name': 'Alice', 'age': 26}


# SET
# ---------

fruits = {"apple", "banana"}
basket = fruits     #same set reference

basket.add("orange")

print(fruits)       # {'apple', 'banana', 'orange'}


# --------------------------------------------------
# IMMUTABLE Types
# --------------------------------------------------


# INTEGER
# -------

a = 10
b = a               # same integer reference

b += 5              # creates a NEW integer object

print(a)  # 10 (unchanged)
print(b)  # 15 


# STRING
# -------

a = "hello"
b = a               # same string reference

b += " world"  #     creates a NEW string

print(a)  # hello (unchanged)
print(b)  # hello world


# TUPLE
# -------

a = (1, 2, 3)
b = a               # same tuple reference

b += (4,)           # creates a NEW tuple

print(a)  # (1, 2, 3)
print(b)  # (1, 2, 3, 4)