#!/usr/bin/env python

# Driver code


class Graph:
    def __init__(self):

        # We will store the graph in a dict
        self.graph = dict()

    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.graph[node1] = []
        self.graph[node1].append(node2)

    # Do breadth first search
    # The idea is that we will keep a queue of visited nodes
    def bfs(self, source):

        # Add the source to the queue first
        queue = [source]
        visited = {node: False for node in self.graph}
        visited[source] = True

        # While we still have nodes in the queue
        while queue:

            source = queue.pop(0)
            print(source, end=" ")

            # We could keep a list, but hash (dict) is faster for lookup

            for node in self.graph[source]:
                if visited[node] == False:
                    queue.append(node)
                    visited[node] = True


# Create a graph
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

g.bfs(2)
