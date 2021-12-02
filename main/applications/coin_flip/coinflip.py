"""Coin Flip:
A program to find out how often
a line of six heads or six tails comes up 
in a randomly generated list of heads and tails."""

import random
streaks = 0

for i in range(10000): # Run experiment multiple times
    HT = [] # Create a lists of 100 heads or tails (flips)

    for j in range(100):
        if random.randint(0,1) == 0:
            HT.append('H')
        else:
            HT.append('T')
    print(HT)
    
    for k in range(len(HT)): # Search streaks of 6 heads or tails

        count = 0
        for m in range(6):
            try:
                if HT[k] == 'H' and HT[k] == HT[k+m]:
                    count += 1
                else:
                    count = 0
                    break
            except IndexError: # item 95
                break

        if count == 6:
            print('\x1b[6;30;42m' + str(HT[k:k+6]) + '\x1b[0m')
            streaks += 1

posibilities = 95 * 10000 # maxim posibilities
percentage = streaks * 100 / posibilities
probability = percentage / 100

print("Streaks: ", streaks)
print("Posibilities: ", posibilities)
print("Probability: ", probability)
print("Math 1/2^6: ", 1/2**6)

# Streaks:  14861
# Posibilities:  950000
# Probability:  0.01564315789473684
# Math 1/2^6:  0.015625