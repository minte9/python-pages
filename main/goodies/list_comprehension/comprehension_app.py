""" List comprehension example
Matrix to tree (arbitrary number of children)
"""

class Node:
    def __init__(self, value=None, children=[]):
        self.value = value
        self.children = children

# For loop
def matrix_to_tree_FL(m):
    if isinstance(m, int):
        return Node(m, [])

    children = []
    for child in m:
        node = matrix_to_tree_FL(child) # Look Here
        children.append(node)

    return Node(None, children)

# List comprehension
def matrix_to_tree_LC(m):
    if isinstance(m, int):
        return Node(m, [])

    children = [matrix_to_tree_LC(child) for child in m] # Look Here
    return Node(None, children)

matrix = [
    [
        [3, 4],
        [8, [-2, 10], 5],
    ],
    7,
]

tree = matrix_to_tree_FL(matrix)
assert tree.children[0].children[0].children[0].value == 3
assert tree.children[0].children[0].children[1].value == 4
assert tree.children[0].children[1].children[0].value == 8
assert tree.children[0].children[1].children[1].children[0].value == -2
assert tree.children[0].children[1].children[1].children[1].value == 10
assert tree.children[1].value == 7

matrix = [
    [3, 4],
    [8, [-2, 10], 5],
    7,
]

tree = matrix_to_tree_LC(matrix)
assert tree.children[0].children[0].value == 3
assert tree.children[0].children[1].value == 4
assert tree.children[1].children[0].value == 8
assert tree.children[1].children[1].children[0].value == -2
assert tree.children[1].children[1].children[1].value == 10
assert tree.children[2].value == 7