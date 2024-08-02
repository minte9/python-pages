""" We can write if/else statements more concisely using conditional expression.
"""

# Conditional expression
a = 0
b = 100 if a >= 0 else -1
print(b) # 100

# Normal use of if/else
a = 0
if a >= 0:
    b = 100
else:
    b = -1
print(b) # 100