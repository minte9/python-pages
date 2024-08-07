""" List comprehension Example
Matrix to tree (arbitrary number of children)
"""

class Node:
    def __init__(self, value=None, children=[]):
        self.value = value
        self.children = children

def matrix_to_tree(m):
    if isinstance(m, int): # Base case
        return Node(m, [])

    """
    children = []
    for child in m:
        node = matrix_to_tree(child) # Recursive case
        children.append(node)
    """

    children = [matrix_to_tree(child) for child in m] # Look Here

    return Node(None, children)

M = [
    [3, 4],
    [8, [-2, 10], 5],
    7,
]

tree = matrix_to_tree(M)

print( tree.children[0].children[0].value )               # 3
print( tree.children[1].children[0].value )               # 8
print( tree.children[1].children[1].children[0].value )   # -2
print( tree.children[2].value )                           # 7