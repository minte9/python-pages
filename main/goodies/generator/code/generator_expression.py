"""
    Generator expression is similar to list, dictionary or set comprehension.
    The expression is enclosed withing parantheses insteed of brackets.
"""

gen = (x**2 for x in range(100))

print(next(gen), end=' ')
print(next(gen), end=' ')
print(next(gen), end=' ')

# This is equivalent to the more verbose generator:

def make_gen():
    for x in range(100):
        yield x**2
gen = make_gen()

print(next(gen), end=' ')
print(next(gen), end=' ')
print(next(gen), end=' ')

"""
    0 1 4 0 1 4 
"""
