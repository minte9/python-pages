# pp134 You {{don't have}} to use str() to convert values to string.
"""String interpolation:
The %s operator inside the string is a marker to be replaced.
"""

name = 'John'
age = 40
message = 'My name is %s and I\'m %s old'

print(message % (name, age))
    # My name is John and I'm 40 old