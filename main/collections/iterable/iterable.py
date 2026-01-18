# -------------------------------
# ITERABLE
# -------------------------------
# In Python:
#   - Iterable: something you can loop over
#   - Iterator: something that produces values one at a time
# 
# Think of it like this:
#   - An iterable is a book
#   - An iterator is a bookmark that remembers where you are
#
# Iterable:
#   - An iterable is an object that can return its elements one at a time.
#
# Examples:
#   - list
#   - string
#   - tuple
#   - dictionary
#   - se
#
# An iterable is an object that can be passed to iter() to produce an iterator.

A = [1, 2, 3]   # list - iterable
I = iter(A)     # crete an iterator from the iterable

# -----------------------------
# ITERATOR
# ------------------------------
# An iterator remembers its current position 
# and knows how to get the next value.
#
# Each call to next() advances the iterator.

print(next(I))  # 1
print(next(I))  # 2
print(next(I))  # 3

# End of iterator
try: 
    print(next(I))
except StopIteration:
    print("StopIteration")


# ------------------------------
# LOOP MECHANISM
# ------------------------------
# A for-loop:
# 1. Calls iter() 
# 2. Calls next() repeatedly
# 3. Stops on Stop Iterator 

A = [1, 2, 3]

for i in A:
    print(i)

# Equivalent to:
# --------------

I = iter(A)

while True:
    try:
        i = next(I)
        print(i)
    except StopIteration:
        break
