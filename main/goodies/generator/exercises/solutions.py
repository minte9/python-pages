"""
    Display a dictionary's keys using loop, iter object and generator expression.
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
    Do the same for values using loop and generator expresession.
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
    Print the sum of the square numbers from 0 to 4.
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
    Create a generator that yields squares of numbers 0 to 9.
"""

def SquareGenerator(n=10):
    for i in range(n):
        yield i**2

G = SquareGenerator()
for x in G:
    print(x, end=' ')
