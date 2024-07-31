"""
    1. Capitalize each letter from a string and put them in a list.  
       Use a single line of code using list comprehension.
"""

S = "Hippopotamus"
R = [s.capitalize() for s in S]
print(sorted(R))
    # ['A', 'H', 'I', 'M', 'O', 'O', 'P', 'P', 'P', 'S', 'T', 'U']

"""
    2. Capitalize each letter from a string and put them in a set.  
       Use a single line of code using set comprehension.
"""

S = "Hippopotamus"
R = {s.capitalize() for s in S}
print(sorted(R))
    # ['A', 'H', 'I', 'M', 'O', 'P', 'S', 'T', 'U']


"""
    3. Use dictionary comprehension to cut in half the items' prices
"""

P = {'milk': 1.02, 'coffe': 2.20}
R = {k: v/2 for (k,v) in P.items()}
print(R)
    # {'milk': 0.51, 'coffe': 1.1}
