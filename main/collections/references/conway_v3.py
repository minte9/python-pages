"""Conway's game of life
More info at: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
Version: 3
Main loop to set next alive or dead squares.
Deep copy is relevant only for compound objects
(objects that contain other objects, like lists or class instances)"""
__version__ = 3
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

while True: # main loop
    print("-------------")
    currC = copy.deepcopy(nextC)  # Look Here
    print_cells(currC)

    for x in range(X):
        for y in range(Y):

            L = (x - 1) % X # Left
            R = (x + 1) % X # Right
            A = (y - 1) % Y # Above
            B = (y + 1) % Y # Below

            n = 0

            if currC[L][A] == '#': # Top left
                n += 1
            if currC[x][A] == '#': # Top
                n += 1
            if currC[R][A] == '#': # Top right
                n += 1
            if currC[R][y] == '#': # Right
                n += 1
            if currC[R][B] == '#': # Bottom right
                n += 1
            if currC[x][B] == '#': # Bottom
                n += 1
            if currC[L][B] == '#': # Bottom left 
                n += 1
            if currC[L][y] == '#': # Left
                n += 1

            # Set cells base on Conway's Game of Life rules:
            if currC[x][y] == '#' and n == 2 or n == 3:
                # Living cells with 2 or 3 neighbors stay alive:
                nextC[x][y] = '#'

            elif currC[x][y] == ' ' and n == 3:
                # Dead cells with 3 neighbors become alive:
                nextC[x][y] = '#'

            else:
                # Everything else dies or stays dead:
                nextC[x][y] = ' '
    
    time.sleep(1)