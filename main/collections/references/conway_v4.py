# Conway game of life - v4
#
# Glider pattern (not random) \
# A pattern that moves diagonally every four steps

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

            if currC[L][A] == '#':
                n += 1
            if currC[x][A] == '#':
                n += 1
            if currC[R][A] == '#':
                n += 1
            if currC[R][y] == '#':
                n += 1
            if currC[R][B] == '#':
                n += 1
            if currC[x][B] == '#':
                n += 1
            if currC[L][B] == '#': 
                n += 1
            if currC[L][y] == '#':
                n += 1

            # Game Rules
            #
            if currC[x][y] == '#' and n == 2 or n == 3:
                nextC[x][y] = '#'

            elif currC[x][y] == ' ' and n == 3:
                nextC[x][y] = '#'

            else:
                nextC[x][y] = ' '
                
    time.sleep(1)