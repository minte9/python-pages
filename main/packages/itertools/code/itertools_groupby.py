""" Groupby
    Make an iterator that returns consecutive keys and groups from the iterable.
"""

import itertools

transactions = [
    {'date': '2024-08-01', 'amount': 100},
    {'date': '2024-08-02', 'amount': 150},
    {'date': '2024-08-01', 'amount': 200},
    {'date': '2024-08-03', 'amount': 50},
]
transactions.sort(key=lambda x: x['date']) # Sort by date


# without itertools
def groupby(items, sortby):
    grouped = {}
    
    for t in items:
        date = t['date']
        if date not in grouped:
            grouped[date] = []
        grouped[date].append(t['amount'])  # Look here
    return grouped

grouped = groupby(transactions, 'date')
print(grouped)


# itertools
grouped = itertools.groupby(transactions, key=lambda x: x['date'])  # iterator
for date, group in grouped:                                         
    print(date, list(group)) # group is a generator

"""
    {'2024-08-01': [100, 200], '2024-08-02': [150], '2024-08-03': [50]}
    2024-08-01 [{'date': '2024-08-01', 'amount': 100}, {'date': '2024-08-01', 'amount': 200}]
    2024-08-02 [{'date': '2024-08-02', 'amount': 150}]
    2024-08-03 [{'date': '2024-08-03', 'amount': 50}]
"""
