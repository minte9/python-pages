"""
Generator expressions is similar to list, dictionary or set comprehension. 
Enclose withing parantheses insteed of brackets
"""

G = (x**2 for x in range(100))

print(next(G)) # 0
print(next(G)) # 1
print(next(G)) # 4

# This is equivalent to the more verbose generator:

def make_gen():
    for x in range(100):
        yield x**2

G = make_gen()

print(next(G)) # 0
print(next(G)) # 1
print(next(G)) # 4