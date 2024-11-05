""" A Dictionary is a data type that stores data in key/value pair
"""

# Input dictionary
prices = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}

# Dictionary comprehension
procent = 0.5
prices_new = {k: v*procent for (k, v) in prices.items() }
print(prices_new)

"""
    {'milk': 0.51, 'coffee': 1.25, 'bread': 1.25}
"""