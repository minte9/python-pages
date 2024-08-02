""" 1. Capitalize each letter from a string and put them in a list.  
       Use a single line of code using list comprehension.
"""

S = "Hippopotamus"
R = [s.capitalize() for s in S]
print(sorted(R))
    # ['A', 'H', 'I', 'M', 'O', 'O', 'P', 'P', 'P', 'S', 'T', 'U']



""" 2. Capitalize each letter from a string and put them in a set.  
       Use a single line of code using set comprehension.
"""

S = "Hippopotamus"
R = {s.capitalize() for s in S}
print(sorted(R))
    # ['A', 'H', 'I', 'M', 'O', 'P', 'S', 'T', 'U']



""" 3. Use dictionary comprehension to cut in half the items' prices
"""

P = {'milk': 1.02, 'coffe': 2.20}
R = {k: v/2 for (k,v) in P.items()}
print(R)
    # {'milk': 0.51, 'coffe': 1.1}



""" 4. Create a function that transform a matrix (list) into a tree (of nodes).  
       Use a Node class (with a value and children list as attributes).  
       Loop recursively through the matrix using a for loop.  
       Do the same using list comprehension.  
"""

M = [
    [3, 4],
    [8, [-2, 10], 5],
    7,
]

class Node:
    def __init__(self, value=None, children=[]):
        self.value = value
        self.children = children

def matrix_to_tree(x):
    if isinstance(x, int): # Base case
        return Node(x, [])

    """
    children = []
    for child in x:
        node = matrix_to_tree(child) # Recursive case (child matrix or int value)
        children.append(node)
    """

    children = [matrix_to_tree(child) for child in x]

    return Node(None, children)

tree = matrix_to_tree(M)
print(tree.children[0].children[0].value) # 3
print(tree.children[1].children[1].children[0].value) # -2