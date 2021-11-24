# Conway game of life - v3
#
# Main loop to set next alive or dead squares \
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

import random, time, copy

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

nextC = get_cells()

# Conway's Game of Life - Loop
#
while True:
    print("-------------")
    currC = copy.deepcopy(nextC)    # new compound object (copies everything)
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