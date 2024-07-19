# Display a dictionary's KEYS using iter object, not through a loop
dict = {'a': 1, 'b': 2}
keys_iter = iter(dict)

print(next(keys_iter)) # a
print(next(keys_iter)) # b

# Display the VALUES using iter object, not through a loop
dict = {'a': 1, 'b': 2}
values_iter = iter(dict.values())

print(next(values_iter)) # 1
print(next(values_iter)) # 2