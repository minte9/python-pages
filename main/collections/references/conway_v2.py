# Conway game of life
#
# v2 - count neighbours
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
#
# The neighbour is wraparound ...
# For x=0, the left neighbour has x=59
#
# The mod-wraparound tehchnique works as well for ...
# right, above, below

import random

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

assert (0 - 1) % 6 == 5  # left neighour (wrap arround)
assert (1 - 1) % 6 == 0
assert (2 - 1) % 6 == 1
assert (3 - 1) % 6 == 2
assert (4 - 1) % 6 == 3
assert (5 - 1) % 6 == 4

assert (0 + 1) % 6 == 1  # right neighbour
assert (1 + 1) % 6 == 2
assert (2 + 1) % 6 == 3
assert (3 + 1) % 6 == 4
assert (4 + 1) % 6 == 5
assert (5 + 1) % 6 == 0

cells = get_cells()
print_cells(cells)

for x in range(X): # x=0 ... x=5
    for y in range(Y):

        left  = (x - 1) % X
        right = (x + 1) % X
        above = (y - 1) % Y
        below = (y + 1) % Y

        neighbours = 0  # maxim 8 neighbours

        if cells [left][above] == '#':    # top left - alive
            neighbours += 1

        if cells [x][above] == '#':       # top
            neighbours += 1

        if cells [right][above] == '#':   # top right
            neighbours += 1

        if cells [right][y] == '#':       # right
            neighbours += 1

        if cells [right][below] == '#':   # bottom right
            neighbours += 1

        if cells [x][below] == '#':       # bottom
            neighbours += 1
            
        if cells [left][below] == '#':    # bottom left
            neighbours += 1

        if cells [left][y] == '#':        # left
            neighbours += 1

        print(str(x) + ":" + str(y), "neighbours:", neighbours)