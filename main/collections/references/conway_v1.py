"""Conway game of life
Displays random alive or dead squares. 
A filled-in square will be "alive" (#)
An empty square will be "dead" (' ')"""
__version__ = 1
import random, time

X = 6
Y = 6

def get_cols():
    cols = []
    for i in range(X):
        row = []
        for j in range(Y):
            if random.randint(0,1) == 0:
                row.append('#')
            else:
                row.append(' ')
        cols.append(row)
    return cols

def print_cols(cols):
    for row in cols:
        print (*row, sep=' ')

while True:
    print_cols(get_cols())
    print("-------------")
    time.sleep(1)