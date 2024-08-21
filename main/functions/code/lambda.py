""" Lambda (or anonymous) functions are used for writing single statement  
    The result of a lambda function is the return value
    It is often less typing (and clearer) to pass a lamda function as opposed to a function
"""

def h(x):
    return x*2
print(h(2))

h = lambda x: x*2
print(h(3))

# Usage example: Sort by the number of distinc letters
S = ['foo', 'card', 'bar', 'aaaa']
S.sort(key=lambda x: len(set(x)))
print(S)

"""
    4
    6
    ['aaaa', 'foo', 'bar', 'card']
"""