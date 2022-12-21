"""String interpolation:
The %s operator inside the string is a marker to be replaced.
"""

name = 'John'
age = 40
message = 'My name is %s and I\'m %s old'

print(message % (name, age))
    # My name is John and I'm 40 old

print("I am %s and have %s dogs " % ("John", 2))
    # I am John and have 2 dogs 