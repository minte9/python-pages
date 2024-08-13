""" Sometimes you want to take input from user until they type quit
"""
  
while True:
    line = input('> ')
    if (line == 'quit'): 
        break
    print(line)

print('Done')