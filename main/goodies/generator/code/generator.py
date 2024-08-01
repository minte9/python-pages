 
"""
    A generator is a simpler way to create an iterator.
    A generator is a function that yields values one at a time.
"""

def SquareGenerator(n=10):
    for i in range(1, n+1):
        yield i**2

G = SquareGenerator()
for x in G:
    print(x, end=' ')

"""
    1 4 9 16 25 36 49 64 81 100 
"""
