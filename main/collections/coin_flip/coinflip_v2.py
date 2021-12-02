"""Coin Flip:
A program to find out how often
a line of six heads or six tails comes up 
in a randomly generated list of heads and tails.
Version 2"""

import random
streaks = 0

for i in range(10000):
    HT = random.choices('HT', k=100)
    
    for k in range(len(HT)):
        
        count = 0
        for m in range(6):
            try:
                if HT[k] == 'H' and HT[k] == HT[k+m]:
                    count += 1
                else:
                    break
            except IndexError: # item 95
                break

        if count == 6:
            streaks += 1

posibilities = 95 * 10000
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