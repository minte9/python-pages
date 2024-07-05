# Input string
str = "abcd"

# For loop without list comprehension
res = []
for c in str:
    if c in ['a', 'b', 'c']:
        res.append(c.capitalize())
print(res)
    # A, B, C

# List comprehension
res2 = [c.capitalize() for c in str if c in ['a', 'b']]
print(res2)
    # A, B

# Set comprehension (curly brackets insteed of square brackets)
myList = ['a', 'b', 'c', 'aa', 'abc']
unique_lenghts = {len(s) for s in myList}
print(unique_lenghts)
    # 1, 2, 3

# Dictionary comprehension
prices = {'milk': 1.02, 'coffe': 2.20}
procent = 0.5
prices_new = {k: v*procent for (k,v) in prices.items()} # items() display the dictionary key/value pair
print(prices_new) 
    # 0.51, 1.10    