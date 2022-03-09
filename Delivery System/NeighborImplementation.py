"""
File for implementing a Nearest Neighbor greedy algorithm.
"""

# Import necessery function
from GraphImplementation import graph

# Function for implementing a nearest neighbor algorithm utilizing the GraphImplementation
# O(n^2)
def Neighbor_Implementation(path):
    # Set paramaters
    location = "HUB"
    sortingPath = path
    edgeWeights = graph.edgeWeight

    # Starts optimal path at HUB
    optimalPath = [location]

    # For each item in path, determines the optimal path based on the edge weights
    # O(n^2)
    while len(sortingPath) != 0:
        min = [0, location]
        for address in sortingPath:
            distance = edgeWeights[optimalPath[-1], address]
            if min[0] == 0:
                min = [distance, address]
            if distance < min[0] and distance != 0:
                min = [distance, address]
        if min[1] not in optimalPath:
            optimalPath.append(min[1])
        sortingPath.remove(min[1])

    return optimalPath