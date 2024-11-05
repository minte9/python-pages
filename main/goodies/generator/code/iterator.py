"""
    An iterator is an object implements the iterator protocol.
    An iterator is an object that contains a countable number of values.
    An interator is any object that will return objects when used in a loop context.
"""

class SquareIterator():
    def __init__(self):
        self.num = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.num < 5:
            res = self.num**2
            self.num += 1
            return res
        else:
            raise StopIteration

print("Iterator usage:")
squares = SquareIterator()
for n in squares:
    print(n, end=' ')
print('\n')

print("Loop through a collection:")
mydict = {'a':1, 'b': 2, 'c': 3}

for key in mydict:  # __next__() is called
    print(key, end=' ')

myiterator = iter(mydict)
print(next(myiterator), end=' ')
print(next(myiterator))

"""
    Iterator usage:
    0 1 4 9 16 

    Loop through a collection:
    a b c a b
"""