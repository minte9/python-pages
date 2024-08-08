""" Traveling Salesman Problem (TSP)
    Find the shortest route that visits a list of cities.
    We can generate all posible routes and find the shortest that visits 
    a list of cities and return to the original city.
"""

from itertools import permutations
from icecream import ic

DEBUG = True
ic.enable() if DEBUG else ic.disable()

# Cities and distances
cities = ['A', 'B', 'C', 'D']
distances = {
    ('A', 'B'): 10, ('A', 'C'): 15, ('A', 'D'): 20, 
    ('B', 'C'): 35, ('B', 'D'): 25,
    ('C', 'D'): 30,
}

# Add return distances (B -> A)
for (a, b), v in list(distances.items()):
    distances[(b, a)] = v
ic(distances)

# Generate all posible routes (permutations of cities)
routes = permutations(cities)
ic(routes)

# Compute total distance
def total_distance(route):
    d = 0

    for i in range(len(route) - 1):
        d += distances[(route[i], route[i+1])]

    # Add the distance back (from the last to the first city)
    d += distances[(route[-1], route[0])]
    return d

# Find the shortes route
shortest_route = None
min_distance = float('inf')

for route in routes:
    curr_distance = total_distance(route)
    ic(route, curr_distance)

    if curr_distance < min_distance:
        min_distance = curr_distance
        shortest_route = route

print(f"The shortest route is {shortest_route} with a distance of {min_distance}")

"""
    ic| distances: {('A', 'B'): 10,
                    ('A', 'C'): 15,
                    ('A', 'D'): 20,
                    ('B', 'A'): 10,
                    ('B', 'C'): 35,
                    ('B', 'D'): 25,
                    ('C', 'A'): 15,
                    ('C', 'B'): 35,
                    ('C', 'D'): 30,
                    ('D', 'A'): 20,
                    ('D', 'B'): 25,
                    ('D', 'C'): 30}

    ic| routes: <itertools.permutations object at 0x0000023204ED4040>
    ic| route: ('A', 'B', 'C', 'D'), curr_distance: 95
    ic| route: ('A', 'B', 'D', 'C'), curr_distance: 80
    ic| route: ('A', 'C', 'B', 'D'), curr_distance: 95
    ic| route: ('A', 'C', 'D', 'B'), curr_distance: 80
    ic| route: ('A', 'D', 'B', 'C'), curr_distance: 95
    ic| route: ('A', 'D', 'C', 'B'), curr_distance: 95
    ic| route: ('B', 'A', 'C', 'D'), curr_distance: 80
    ic| route: ('B', 'A', 'D', 'C'), curr_distance: 95
    ic| route: ('B', 'C', 'A', 'D'), curr_distance: 95
    ic| route: ('B', 'C', 'D', 'A'), curr_distance: 95
    ic| route: ('B', 'D', 'A', 'C'), curr_distance: 95
    ic| route: ('B', 'D', 'C', 'A'), curr_distance: 80
    ic| route: ('C', 'A', 'B', 'D'), curr_distance: 80
    ic| route: ('C', 'A', 'D', 'B'), curr_distance: 95
    ic| route: ('C', 'B', 'A', 'D'), curr_distance: 95
    ic| route: ('C', 'B', 'D', 'A'), curr_distance: 95
    ic| route: ('C', 'D', 'A', 'B'), curr_distance: 95
    ic| route: ('C', 'D', 'B', 'A'), curr_distance: 80
    ic| route: ('D', 'A', 'B', 'C'), curr_distance: 95
    ic| route: ('D', 'A', 'C', 'B'), curr_distance: 95
    ic| route: ('D', 'B', 'A', 'C'), curr_distance: 80
    ic| route: ('D', 'B', 'C', 'A'), curr_distance: 95
    ic| route: ('D', 'C', 'A', 'B'), curr_distance: 80
    ic| route: ('D', 'C', 'B', 'A'), curr_distance: 95

    The shortest route is ('A', 'B', 'D', 'C') with a distance of 80
"""
