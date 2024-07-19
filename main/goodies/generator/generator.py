"""
    A normal function execute and return a single result at a time.
    A generator can return a sequence of values by pausing and resuming execution.
"""

def squares(n=10):
    print("Generating squares from 1 to", n**2)
    for i in range(1, n+1):
        yield i**2

mygen = squares()
for x in mygen:
    print(x, end=' ')
        # Generating squares from 1 to 100
        # 1 4 9 16 25 36 49 64 81 100
