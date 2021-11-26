"""Conway game of life
Glider pattern (not random).
A pattern that moves diagonally every four steps"""
__version__ = 4
import time, copy

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

            L = (x - 1) % X # left
            R = (x + 1) % X # right
            A = (y - 1) % Y # above
            B = (y + 1) % Y # below

            n = 0

            if currC[L][A] == ALIVE: # top left
                n += 1
            if currC[x][A] == ALIVE: # top
                n += 1
            if currC[R][A] == ALIVE: # top right
                n += 1
            if currC[R][y] == ALIVE: # right
                n += 1
            if currC[R][B] == ALIVE: # bottom right
                n += 1
            if currC[x][B] == ALIVE: # bottom
                n += 1
            if currC[L][B] == ALIVE: # bottom left 
                n += 1
            if currC[L][y] == ALIVE: # left
                n += 1

            if currC[x][y] == ALIVE and n == 2 or n == 3: # game rules
                nextC[x][y] = ALIVE

            elif currC[x][y] == ' ' and n == 3:
                nextC[x][y] = ALIVE

            else:
                nextC[x][y] = DEAD
                
    time.sleep(1)