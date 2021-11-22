# A list contains multiple values in an ordered sequence
#
# Unlike strings, list are mutable, they can be changes

numbers = [1, 2]
numbers[1] = 3

assert numbers == [1, 3]
assert numbers != [1, 2]