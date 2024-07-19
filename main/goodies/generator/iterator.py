"""
Many objects in Python support iteration.
They are using iteration protocol, a generic way to make objects iterable.
An interator is any object that will yield objects when used in a loop context.
"""

# Loop context
dict = {'a':1, 'b': 2, 'c': 3}
for key in dict:
    print(key)
        # a (yield, iterator object caled)
        # b
        # c

# Iterator object
itr = iter(dict)
print(itr)
    # <dict_keyiterator object at 0x00000274B8582900>

# Loop equivalent
print(next(itr)) # a
print(next(itr)) # b
print(next(itr)) # c