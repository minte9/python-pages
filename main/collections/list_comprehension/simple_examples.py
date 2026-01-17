""" LIST COMPREHENSION - EXAMPLES
---------------------------------
1. Capitalize each letter from a string and put them in a list.  
   Use a single line of code using list comprehension.  
      S = "Hippopotamus"  

2. Capitalize each letter from a string and put them in a set.  
   Use a single line of code using set comprehension.  
      S = "Hippopotamus" 

3. Use dictionary comprehension to cut in half the items' prices  
      P = {'milk': 1.02, 'coffe': 2.20}
"""


""" Capitalize each letter (list)
"""
str = "Hippopotamus"
L = [s.capitalize() for s in str]
print(L) 
    # ['H', 'I', 'P', 'P', 'O', 'P', 'O', 'T', 'A', 'M', 'U', 'S']


""" Capitalize each letter (set)
"""
str = "Hippopotamus"
S = {s.capitalize() for s in str}  # unsorted
S = sorted(S)
print(S)  
    # ['A', 'H', 'I', 'M', 'O', 'P', 'S', 'T', 'U']


""" Half prices
"""
prices = {'milk': 1.02, 'coffee': 2.20}
P = {k: v/2 for (k,v) in prices.items()}
print(P)  
    # {'milk': 0.51, 'coffee': 1.1}