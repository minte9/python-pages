"""Conway's game of life
More info at: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
Version 2:
Count cell neighbours (8 maximum).
The neighbours are wraparound, for x=0, the left neighbour has x=59
The mod-wraparound technique works as well for right, above, below"""

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

assert (0 - 1) % 6 == 5  # Left neighour (wrap arround)
assert (1 - 1) % 6 == 0
assert (2 - 1) % 6 == 1
assert (3 - 1) % 6 == 2
assert (4 - 1) % 6 == 3
assert (5 - 1) % 6 == 4

assert (0 + 1) % 6 == 1  # Right neighbour
assert (1 + 1) % 6 == 2
assert (2 + 1) % 6 == 3
assert (3 + 1) % 6 == 4
assert (4 + 1) % 6 == 5
assert (5 + 1) % 6 == 0

cells = get_cells()
print_cells(cells)

for x in range(X): # x=0 ... x=5
    for y in range(Y):

        left  = (x - 1) % X  # Look Here
        right = (x + 1) % X
        above = (y - 1) % Y
        below = (y + 1) % Y

        neighbours = 0  # Maxim 8 neighbours

        if cells [left][above] == '#':    # Top left - alive
            neighbours += 1

        if cells [x][above] == '#':       # Top
            neighbours += 1

        if cells [right][above] == '#':   # Top right
            neighbours += 1

        if cells [right][y] == '#':       # Right
            neighbours += 1

        if cells [right][below] == '#':   # Bottom right
            neighbours += 1

        if cells [x][below] == '#':       # Bottom
            neighbours += 1
            
        if cells [left][below] == '#':    # Bottom left
            neighbours += 1

        if cells [left][y] == '#':        # Left
            neighbours += 1

        print(str(x) + ":" + str(y), "neighbours:", neighbours)