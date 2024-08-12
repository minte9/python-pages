""" Compress
    Makes an interator that returns elements where the corresponding item is true.  
    Filtering with a Boolean list (example).
"""

import itertools

products = ['apple', 'banana', 'cherry', 'orange']
in_stock = [True, False, True, False]


# without itertools
available_products = [item for item, available in zip(products, in_stock) if available]
print(available_products)


# itertools
available_products = itertools.compress(products, in_stock)  # iterator
print(list(available_products))

"""
    ['apple', 'cherry']
    ['apple', 'cherry']
"""