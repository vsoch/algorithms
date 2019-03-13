#!/usr/bin/env python

# Option 1- with queue

class Graph:

    def __init__(self):
        self.graph = dict()

    def add_edge(self, key, value):
        if key not in self.graph:
            self.graph[key] = []
        self.graph[key].append(value)

    def dfs(self, source):

        # Make a queue and add the source to it
        queue = [source]
 
        # All nodes aren't visited
        visited = {node: False for node in self.graph}

        while queue:

            # Important removes from end!
            source = queue.pop(-1)
            visited[source] = True
            print(source)
            for node in self.graph[source]:    
                if not visited[node]:
                    visited[node] = True
                    queue.append(node)


# Create a graph
g = Graph() 
g.add_edge(0, 1) 
g.add_edge(0, 2) 
g.add_edge(1, 2) 
g.add_edge(2, 0) 
g.add_edge(2, 3) 
g.add_edge(3, 3) 
  
g.dfs(2)

print()

# Option 2 - with recursion, helper function

class Graph:

    def __init__(self):
        self.graph = dict()

    def add_edge(self, key, value):
        if key not in self.graph:
            self.graph[key] = []
        self.graph[key].append(value)

    def dfs_helper(self, source, visited):

        visited[source] = True
        print(source)
        for node in self.graph[source]:
            if visited[node] == False:
                visited[node] = True
                self.dfs_helper(node, visited)

    # This is the main function
    def dfs(self, source):

        visited = {node: False for node in self.graph}
        
        # Call helper function
        self.dfs_helper(source, visited)

# Create a graph
g = Graph() 
g.add_edge(0, 1) 
g.add_edge(0, 2) 
g.add_edge(1, 2) 
g.add_edge(2, 0) 
g.add_edge(2, 3) 
g.add_edge(3, 3) 
  
g.dfs(2)
