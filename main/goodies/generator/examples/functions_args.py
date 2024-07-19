"""
Generators are often used with functions like sum, max, min.
A function is called using parentheses ().
"""

y = sum(x**2 for x in range(5))
print(y)
    # x = 0, 1, 2, 3, 4
    # y = 0 + 1 + 4 + 9 + 16 = 30

# Square brackets are used for list comprehensions and indexing
y = sum([x**2 for x in range(5)])
print(y)
    # 30

# Finding max using generator
y = max(x/2 for x in [10, 50, 20, 30])
print(y)
    # 25.0