""" LIST COMPREHENSION - EXAMPLES (advanced)
--------------------------------------------
Goal:
Transform a nested list (matrix) into a tree of Node objects.

Rules:
- Each integer becomes a leaf node.
- Each list becomes an internal node 
- The node' children are recursively built from the elemements of that list. 

Never use mutable objects (like []) as default arguments.
"""

M = [
    [3, 4],
    [8, [-2, 10], 5],
    7,
]

class Node():
    """ 
    A tree node.
    Attributes:
        value -> holds an integer (for leaf nodes)
        children -> list of child Node objects (for internal nodes)
    """
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = children if children is not None else []

def matrix_to_tree(x):
    """
    Recursevely converts a nested list (matrix) into a tree of Nodes.
    Parameter:
        x -> can be either:
            - an integer (base case)
            - a list containing integers of other lists (recursive case)
    Returns:
        A Node representing the subtree rooted as x
    """

    # ---- BASE CASE ----
    # If x is an integer, create a leaf node with no children
    if isinstance(x, int):
        return Node(x, [])
    
    # ---- RECURSIVE CASE ----
    # If x is a list, recursively convert each element into a Node
    # and collect them as children.

    # Equivalent "classic" for-loop version:
    
    # children = []
    # for child in x:
    #    node = matrix_to_tree(child)  # Recursive case (return list or int)
    #    children.append(node)
    

    # List comprehension version (more concise, same logic):
    children = [matrix_to_tree(child) for child in x]

    # Internal node: no value, only children
    return Node(None, children)


# Build the tree
tree = matrix_to_tree(M)

# Accessing values inside the tree
print( tree.children[0].children[0].value )               # 3
print( tree.children[1].children[0].value )               # 8
print( tree.children[1].children[1].children[0].value )   # -2
print( tree.children[2].value )                           # 7

