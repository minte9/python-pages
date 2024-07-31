"""
    1. Display a dictionary's keys using loop, iter object and generator expression.
"""
DICT = {'a': 1, 'b': 2}

# Loop
for k, v in DICT.items():
    print(k)

# Iterator
iter = iter(DICT)
print(next(iter))
print(next(iter))

# Generator expression
G = (k for k in DICT)
print(next(G))
print(next(G))


"""
    2. Do the same for values using loop and generator expresession.
"""
DICT = {'a': 1, 'b': 2}

# Loop
for v in DICT.values():
    print(v)

# Generator expression
G = (v for v in DICT.values())
print(next(G))
print(next(G))


"""
    3. Print the sum of the square numbers from 0 to 4.
       Use generator expresion first, then list comprehension.
"""

# Generator expression
y = sum(x**2 for x in range(5))
print(y) 
    # 30

# List comprehension
y = sum([x**2 for x in range(5)])
print(y)
    # 30


"""
    4. Create a generator that yields squares of numbers 0 to 9.
"""

def SquareGenerator(n=10):
    for i in range(n):
        yield i**2

G = SquareGenerator()
for x in G:
    print(x, end=' ')
        # 0 1 4 9 16 25 36 49 64 81


"""
    5. For a list of 30 items, display chunks of 10 using a generator.
"""

def chunks_generator(data, size=10):
    for i in range(0, len(data), size):
        yield data[i:i + size]

G = chunks_generator(list(range(30)))
for chunk in G:
    print(chunk)
        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        # [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
