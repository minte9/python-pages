# ---------------------------------
# MEMORY EFFICIENCY
# ---------------------------------
# An iterator is more efficient than a for loop, 
# because it does not store the collection in memory.

import sys

numbers = list(range(1_000_000))

# Loop
m = sys.getsizeof(numbers)
for n in numbers:
    if n == 10:
        print("Loops: ", n)
        print("Memory:", m) # 8 MB
        break

# Loops:  10
# Memory: 8000056

# Iterator
m = 0
iterator = iter(numbers)
while True:
    n = next(iterator)
    m += sys.getsizeof(n)
    if n == 10:
        print("Iterations: ", n)
        print("Memory:", m) # 300 bytes
        break

# Iterantions:  10
# Memory: 304