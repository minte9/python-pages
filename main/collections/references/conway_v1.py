# Conway game of life - v1
#
# Display random alive or dead squares \
# 
# A filled-in square will be "alive" (#)
# An empty square will be "dead" (' ')
#
# If a living square has 2 or 3 living neighbours, \
# it continures to be alive on the next step.
#
# If a dead square has 3 living neighbours, \
# it comes alive on the next step.
#
# Every other square dies or remains dead \
# on the next step. 

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