""" List comprehension example
Matrix to tree (arbitrary number of children)
"""

class Node:
    def __init__(self, value=None, children=[]):
        self.value = value
        self.children = children

def matrix_to_tree(m, method='for_loop'):
    if isinstance(m, int):
        return Node(m, [])

    if (method == 'for_loop'):
        children = []
        for child in m:
            node = matrix_to_tree(child)
            children.append(node)

    if (method == 'list_comprehension'):
        children = [matrix_to_tree(child) for child in m]

    return Node(None, children)

matrix = [
    [
        [3, 4],
        [8, [-2, 10], 5],
    ],
    7,
]

tree = matrix_to_tree(matrix, 'for_loop')
assert tree.children[0].children[0].children[0].value == 3
assert tree.children[0].children[0].children[1].value == 4
assert tree.children[0].children[1].children[0].value == 8
assert tree.children[0].children[1].children[1].children[0].value == -2

matrix = [
    [3, 4],
    [8, [-2, 10], 5],
    7,
]

tree = matrix_to_tree(matrix, 'list_comprehension')
assert tree.children[0].children[0].value == 3
assert tree.children[0].children[1].value == 4
assert tree.children[1].children[0].value == 8
assert tree.children[1].children[1].children[0].value == -2
assert tree.children[1].children[1].children[1].value == 10
assert tree.children[2].value == 7