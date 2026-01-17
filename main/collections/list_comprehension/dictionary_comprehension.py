""" DICTIONARY COMPREHENSION
----------------------------
A Dictionary is a data type that stores data in key/value pair.
"""

prices = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}  # dictionary

new_prices = {k: v*0.5 for (k, v) in prices.items()}  # compute new prices (procent = 0.5)

print(new_prices)  # {'milk': 0.51, 'coffee': 1.25, 'bread': 1.25}