# Conditional statement
# short expression

n = 0
y = 0

# Conditional expression - normal use

if n > 0:
    y = 100
else:
    y = -1

assert y == -1
assert y != 100


# Conditional expression - concise

n = 1
y = 100 if n > 0 else -1

assert y != -1
assert y == 100