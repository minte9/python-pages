""" Transactions report (itertools.groupby example)
Generate a simple daily report of total credits and debits
"""

import itertools
from operator import itemgetter
from icecream import ic

DEBUG = 1

transactions = [
    {'date': '2024-08-01', 'amount': 100, 'type': 'credit'},
    {'date': '2024-08-01', 'amount': 200, 'type': 'debit'},
    {'date': '2024-08-02', 'amount': 150, 'type': 'credit'},
    {'date': '2024-08-02', 'amount': 50, 'type': 'debit'},
    {'date': '2024-08-03', 'amount': 250, 'type': 'credit'},
    {'date': '2024-08-01', 'amount': 300, 'type': 'credit'},
]

# Sort transactions (by date)
transactions.sort(key=itemgetter('date'))

# Group transactions (by date)
grouped = itertools.groupby(transactions, key=itemgetter('date'))  # Look here

# Totals (amout, credit)
for date, group in grouped:  # grouped is an iterator
    group_list = list(group)
    
    credit_total = sum(x['amount'] for x in group_list if x['type'] == 'credit')
    debit_total = sum(x['amount'] for x in group_list if x['type'] == 'debit')

    ic(date, credit_total, debit_total)

"""
    ic| date: '2024-08-01', credit_total: 400, debit_total: 200
    ic| date: '2024-08-02', credit_total: 150, debit_total: 50
    ic| date: '2024-08-03', credit_total: 250, debit_total: 0
"""


if DEBUG:
    print("""
        DEBUG / Transactions grouped by date:

        You need to assign the iterator to a new variable.
        Once you convert group (generator) to a list and iterate over it, 
        you cannot iterate over it again.
    """);

    grouped = itertools.groupby(transactions, key=itemgetter('date'))  # grouped is an iterator
    
    for date, group in grouped:
        ic(date, list(group))

        """
            ic| date: '2024-08-01'
                list(group): [
                            {'amount': 100, 'date': '2024-08-01', 'type': 'credit'},
                            {'amount': 200, 'date': '2024-08-01', 'type': 'debit'},
                            {'amount': 300, 'date': '2024-08-01', 'type': 'credit'}]
            ic| date: '2024-08-02'
                list(group): [
                            {'amount': 150, 'date': '2024-08-02', 'type': 'credit'},
                            {'amount': 50, 'date': '2024-08-02', 'type': 'debit'}]
            ic| date: '2024-08-03'
                list(group): [{'amount': 250, 'date': '2024-08-03', 'type': 'credit'}]
        """

if DEBUG:
    print("""
        DEBUG / operator.itemgetter (explained):

        operator.itemgetter creates a callable (function) that retrive a specific item
        https://docs.python.org/3/library/operator.html
    """);
    
    date_getter = lambda x: x['date'] # OR
    date_getter = itemgetter('date')  # callable function

    for x in transactions:
        ic(date_getter(x))

        """
            ic| date_getter(x): '2024-08-01'
            ic| date_getter(x): '2024-08-01'
            ic| date_getter(x): '2024-08-01'
            ic| date_getter(x): '2024-08-02'
            ic| date_getter(x): '2024-08-02'
            ic| date_getter(x): '2024-08-03'
        """

if DEBUG:
    print("""
        DEBUG / Sum calculation (explained)
    """);

    grouped = itertools.groupby(transactions, key=itemgetter('date'))

    for date, group in grouped:
        group_list = list(group)

        credit, debit = 0, 0
        for x in group_list:

            if x['type'] == 'credit':
                credit += x['amount']
            elif x['type'] == 'debit':
                debit += x['amount']

        print(f"{date} / Total credit: {credit} / Total debit: {debit}")
