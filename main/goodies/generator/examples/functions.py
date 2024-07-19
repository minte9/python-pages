# Generators are often used ...
# with functions like sum, max, min

y = sum(range(5)) # 0 + 1 + 2 + 3 + 4
assert y == 10
assert y != 15

y = sum(x**2 for x in range(5)) # generator
    # 0 + 2 + 4 + 8 + 16
assert y == 30
assert y != 10

y = max([1, 10, 2, 3])
assert y == 10
assert y != 3

y = max(x/2 for x in [10, 50, 20, 30])
assert y == 25.0
assert y != 15.0