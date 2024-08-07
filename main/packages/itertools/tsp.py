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
