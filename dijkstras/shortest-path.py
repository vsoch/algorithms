#!/usr/bin/env python

# https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/

import sys


class Graph:

    # on init, we have a number of vertices
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for col in range(vertices)] for row in range(vertices)]

    def printSolution(self, dist):
        for node in range(self.V):
            print(node, "t", dist[node])

    # For points not in shortest path set (sptSet)
    # find the vertex with the minimum distance value
    # This will always be the first (0) on first iteration
    # From here we want to return a minimum index
    def minDistance(self, dist, sptSet):

        init = sys.maxsize

        for vertex in range(self.V):
            if dist[vertex] < init and sptSet[vertex] == False:
                init = dist[vertex]
                min_index = vertex

        return min_index

    # Find the shortest path, starting at a source
    def dijkstra(self, source):

        # Give each vertice infinite distance from the source
        dist = [sys.maxsize] * self.V

        # The distance of the source from itself is 0
        dist[source] = 0

        # The shortest path set, none are included to start
        sptSet = [False] * self.V

        # Iterate through the number of vertices
        for idx in range(self.V):

            # Get the index of the smallest distance
            min_index = self.minDistance(dist, sptSet)

            # Put the minimum distance vertex in the
            # shotest path tree
            sptSet[min_index] = True

            # Look through the distances, starting at the min_index
            for v in range(self.V):

                # Must be a distance (>0)   AND  not included in smallest distance set
                # if the distance at the min index plus the actual distance is smaller than the known distance
                if (
                    self.graph[min_index][v] > 0
                    and sptSet[v] == False
                    and (dist[min_index] + self.graph[min_index][v]) < dist[v]
                ):

                    # Update the shortest distance known so far to be this new (smaller) distance
                    dist[v] = dist[min_index] + self.graph[min_index][v]

        self.printSolution(dist)


# Driver program
g = Graph(9)
g.graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0],
]

g.dijkstra(0)
