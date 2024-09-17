""" Transactions report (itertools.groupby example)
Generate a simple daily report of total credits and debits
"""

import itertools
from operator import itemgetter

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
grouped = itertools.groupby(transactions, key=itemgetter('date'))  # grouped is an iterator

totals = []
for date, group in grouped:
    group_list = list(group)
    
    credit = sum(x['amount'] for x in group_list if x['type'] == 'credit')
    debit  = sum(x['amount'] for x in group_list if x['type'] == 'debit')

    totals.append({'date': date, 'total_credit': credit, 'total_debit': debit})

for item in totals:
    print(f"{item['date']} / Total credit: {item['total_credit']} / Total debit: {item['total_debit']}")

"""
    2024-08-01 / Total credit: 400 / Total debit: 200
    2024-08-02 / Total credit: 150 / Total debit: 50
    2024-08-03 / Total credit: 250 / Total debit: 0
"""


from icecream import ic
DEBUG = 1

if DEBUG:
    print("""
        DEBUG / Transactions grouped by date:

        You need to assign the list of a generator to a new variable
        Once you convert group (generator) to a list and iterate over it, 
        you cannot iterate over it again
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
