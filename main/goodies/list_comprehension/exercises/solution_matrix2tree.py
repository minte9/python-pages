M = [
    [3, 4],
    [8, [-2, 10], 5],
    7,
]

class Node:
    def __init__(self, value=None, children=[]):
        self.value = value
        self.children = children

def matrix2tree(m):
    if isinstance(m, int): # Base case
        return Node(m, [])

    """
    children = []
    for v in m:
        node = matrix2tree(v) # Recursive case
        children.append(node)
    """

    children = [matrix2tree(v) for v in m]

    return Node(None, children)

tree = matrix2tree(M)

print( tree.children[0].children[0].value )               # 3
print( tree.children[1].children[1].children[0].value )   # -2