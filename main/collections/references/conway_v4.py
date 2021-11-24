# Conway game of life - v4
#
# Glider pattern (not random)
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
#
# The neighbour is wraparound \
# For x=0, the left neighbour has x=59
#
# The mod-wraparound tehchnique works as well for \
# right, above, below
# 
# Deep copy is relevant only for compound objects \
# (objects that contain other objects, like lists or class instances)
#
# The glider pattern, results in a pattern that \
# moves diagonally every four steps

import time, copy

X = 6
Y = 6

def get_cells():
    cells = []
    for x in range(X):
        row = []
        for y in range(Y):
            if (x, y) in ((1,0), (2,1), (0,2), (1,2), (2,2)):  # Look Here
                row.append('#')
            else:
                row.append(' ')
        cells.append(row)
    return cells

def print_cells(cells):
    for row in cells:
        print (*row, sep=' ')

nextC = get_cells()

while True:
    print("-------------")
    currC = copy.deepcopy(nextC)
    print_cells(currC)

    for x in range(X):
        for y in range(Y):

            L = (x - 1) % X
            R = (x + 1) % X
            A = (y - 1) % Y
            B = (y + 1) % Y

            n = 0

            if currC[L][A] == '#':  # top left
                n += 1
            if currC[x][A] == '#':  # top
                n += 1
            if currC[R][A] == '#':  # top right
                n += 1
            if currC[R][y] == '#':  # right
                n += 1
            if currC[R][B] == '#':  # bottom right
                n += 1
            if currC[x][B] == '#':  # bottom
                n += 1
            if currC[L][B] == '#':  # bottom left 
                n += 1
            if currC[L][y] == '#':  # left
                n += 1

            # Game Rules
            #
            if currC[x][y] == '#' and n == 2 or n == 3:
                nextC[x][y] = '#' # stay alive

            elif currC[x][y] == ' ' and n == 3:
                nextC[x][y] = '#' # dead cells become alive

            else:
                nextC[x][y] = ' ' # everything else dies or stays dead
                
    time.sleep(1)