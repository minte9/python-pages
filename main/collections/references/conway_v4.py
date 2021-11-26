"""Conway's game of life
More info at: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
Version 4:
Glider pattern (not random).
A pattern that moves diagonally every four steps"""

import time, copy, sys

X = 6
Y = 6

ALIVE = '#'
DEAD = ' '

def get_cells():
    cells = []
    for x in range(X):
        row = []
        for y in range(Y):
            if (x, y) in ((1,0), (2,1), (0,2), (1,2), (2,2)):  # Look Here
                row.append(ALIVE)
            else:
                row.append(DEAD)
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

            L = (x - 1) % X # Left
            R = (x + 1) % X # Right
            A = (y - 1) % Y # Above
            B = (y + 1) % Y # Below

            n = 0

            if currC[L][A] == ALIVE: # Top left
                n += 1
            if currC[x][A] == ALIVE: # Top
                n += 1
            if currC[R][A] == ALIVE: # Top right
                n += 1
            if currC[R][y] == ALIVE: # Right
                n += 1
            if currC[R][B] == ALIVE: # Bottom right
                n += 1
            if currC[x][B] == ALIVE: # Bottom
                n += 1
            if currC[L][B] == ALIVE: # Bottom left 
                n += 1
            if currC[L][y] == ALIVE: # Left
                n += 1

            # Set cells base on Conway's Game of Life rules:
            if currC[x][y] == ALIVE and n == 2 or n == 3:
                # Living cells with 2 or 3 neighbors stay alive:
                nextC[x][y] = ALIVE

            elif currC[x][y] == ' ' and n == 3:
                # Dead cells with 3 neighbors become alive:
                nextC[x][y] = ALIVE

            else:
                # Everything else dies or stays dead:
                nextC[x][y] = DEAD

    try:         
        time.sleep(1)
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.