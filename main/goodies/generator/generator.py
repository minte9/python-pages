"""
    A normal function execute and return a single result at a time.
    A generator can return a sequence of values by pausing and resuming execution.
"""

# Functions return values
def squares_func():
    lst = []
    for i in range(1, 10):
        m = i**2
        lst.append(m)
    return lst

print("\nLooping through the function returned value:")
A = squares_func()
for x in A:
    print(x, end=' ')
        # 1 4 9 16 25 36 49 64 81 100


# Generators yield values
def squares_gen():
    for i in range(1, 10):
        yield i**2

print("\nLooping using iter object:")
G = squares_gen()
itr = iter(G)
for i in range(0, 3):
    print(next(itr), end=' ')
        # 1 4 9
