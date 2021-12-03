"""f-string:
Is similar to string interpolation, except that ...
braces are used insteed of %s
The same result can be obtain using format() method.
"""

name = 'John'
age = 40
message = f'My name is {name} and I\'m {age} old'

print(message)
    # My name is John and I'm 40 old

print('My name is {} and I am {} old'.format(name, age))
    # My name is John and I am 40 old

print('My name is {0}'.format(name, age))
    # My name is John