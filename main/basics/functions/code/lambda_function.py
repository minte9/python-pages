""" Lambda (or anonymous) functions
    The result of a lambda function is the return value
    Less typing (and clearer) to pass a lamda function
"""

def short_function(x):
    return x*2

equiv_function = lambda x: x*2

# Example, sort by the number of distinc letters
strings = ['foo', 'card', 'bar', 'aaaa']
strings.sort(key=lambda x: len(set(x)))

print(strings)
    # ['aaaa', 'foo', 'bar', 'card']
