""" Transactions report
    Generate a simple daily report of total credits and debits.

Itemgetter creates a callable (function) that retrive a specific item.
    https://docs.python.org/3/library/operator.html

You need to assign the list of a generator to a new variable.
Once you convert group (generator) to a list and iterate over it, you cannot iterate over it again.
"""

from itertools import groupby
from operator import itemgetter
from icecream import ic

DEBUG = 0
ic.enable() if DEBUG else ic.disable()

transactions = [
    {'date': '2024-08-01', 'amount': 100, 'type': 'credit'},
    {'date': '2024-08-01', 'amount': 200, 'type': 'debit'},
    {'date': '2024-08-02', 'amount': 150, 'type': 'credit'},
    {'date': '2024-08-02', 'amount': 50, 'type': 'debit'},
    {'date': '2024-08-03', 'amount': 250, 'type': 'credit'},
    {'date': '2024-08-01', 'amount': 300, 'type': 'credit'},
]

""" operator.itemgetter (explained)

date_getter = lambda x: x['date'] # OR
date_getter = itemgetter('date')  # callable function

for t in transactions:
    print(date_getter(t))
        # 2024-08-01, 2024-08-01, 2024-08-02, 2024-08-02, 2024-08-03, 2024-08-01
        
# one line
print([itemgetter('date')(x) for x in transactions])
    # [2024-08-01, 2024-08-01, 2024-08-02, 2024-08-02, 2024-08-03, 2024-08-01]
"""

# Sort transactions (by date)
transactions.sort(key=itemgetter('date'))

# Group transactions (by date)
grouped = groupby(transactions, key=itemgetter('date'))

# Generate the report (totals)
for date, group in grouped:

    # Assign to a new variable 
    group_list = list(group)  # Look Here
    ic(date, group_list)
    
    """
    credit = 0
    debit = 0
    for t in group_list:
        if t['type'] == 'credit':
            credit += t['amount']
        elif t['type'] == 'debit':
            debit += t['amount']
    """

    credit = sum(t['amount'] for t in group_list if t['type'] == 'credit')
    debit  = sum(t['amount'] for t in group_list if t['type'] == 'debit')

    print(f"{date} / Total credit: {credit} / Total debit: {debit}")

"""
    2024-08-01 / Total credit: 400 / Total debit: 200
    2024-08-02 / Total credit: 150 / Total debit: 50
    2024-08-03 / Total credit: 250 / Total debit: 0
"""
