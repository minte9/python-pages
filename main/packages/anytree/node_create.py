from anytree import Node, RenderTree

root = Node('A')
node1 = Node('B', parent=root)
node2 = Node('C', parent=root)

for pre, fill, node in RenderTree(root):
    print(pre, node.name)

"""
    A
    ├──  B
    └──  C
"""