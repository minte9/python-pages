""" Matrix list to tree
Tree with arbitrary number of children
"""

class Node:
    def __init__(self, value=None, children=[]):
        self.value = value
        self.children = children

def matrix_to_tree(m):
    if isinstance(m, int):
        return Node(m, []) # Base case

    children = []
    for child in m:
        sub_node = matrix_to_tree(child) # Recursive case
        children.append(sub_node) 

    # children = [matrix_to_tree(child) for child in m] // online
    return Node(None, children)

matrix = [
    [
        [3, 4],
        [8, [-2, 10], 5],
    ],
    7,
]

tree = matrix_to_tree(matrix)
assert tree.children[0].children[0].children[0].value == 3
assert tree.children[0].children[0].children[1].value == 4
assert tree.children[0].children[1].children[0].value == 8
assert tree.children[0].children[1].children[1].children[0].value == -2