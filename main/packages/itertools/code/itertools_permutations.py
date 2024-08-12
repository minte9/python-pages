""" Permutations
    Return successive r length permutations of elements from the iterable.
    permutations('ABCD', 2) → AB AC AD BA BC BD CA CB CD DA DB DC
    permutations(range(3)) → 012 021 102 120 201 210
"""

import itertools

iter = itertools.permutations('ABCD', 2)
print([a + b for a, b in list(iter)])

iter = itertools.permutations(range(3))
print([f"{x}{y}{z}" for x, y, z in list(iter)])

"""
    ['AB', 'AC', 'AD', 'BA', 'BC', 'BD', 'CA', 'CB', 'CD', 'DA', 'DB', 'DC']
    ['012', '021', '102', '120', '201', '210']
"""