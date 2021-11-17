# Unlike strings, list are mutable
# It can be changed

numbers = [1, 2]
numbers[1] = 3

assert numbers == [1, 3]
assert numbers != [1, 2]