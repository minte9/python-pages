# Conway game of life
# --------------------------------------
# A filled-in square will be "alive" (#)
# An empty square will be "dead" (' ')
#
# If a living square has 2 or 3 living neighbours, ...
# it continures to be alive on the next step.
#
# If a dead square has 3 living neighbours, ...
# it comes alive on the next step.
#
# Every other square dies or remains dead ...
# on the next step. 
# --------------------------------------

import random, time, copy, sys

X = 6
Y = 6

def get_cells():
    cells = []
    for i in range(X):
        row = []
        for j in range(Y):
            if random.randint(0,1) == 0:
                row.append('#')
            else:
                row.append(' ')
        cells.append(row)
    return cells

def print_cells(cells):
    for row in cells:
        print (*row, sep=' ')

cells = get_cells()
print_cells(cells)

for x in range(X):
    for y in range(Y):

        left  = x - 1 if x - 1 > 0 else x
        right = x + 1 if x + 1 < X else x
        above = y - 1 if y - 1 > 0 else y
        below = y + 1 if y + 1 < Y else y

        neighbours = 0

        if cells [left][above] == '#':    # top left - alive
            neighbours += 1

        if cells [x][above] == '#':       # top
            neighbours += 1

        if cells [right][above] == '#':   # top right
            neighbours += 1

        if cells [left][y] == '#':        # left
            neighbours += 1

        if cells [right][y] == '#':       # right
            neighbours += 1

        if cells [left][below] == '#':    # bottom left
            neighbours += 1

        if cells [x][below] == '#':       # bottom
            neighbours += 1
            
        if cells [right][below] == '#':   # bottom right
            neighbours += 1

        print(x, y, neighbours)
    print("---")