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
            source = queue.pop()
            print(source)
            for node in self.graph[source]:    
                if not visited[node]:
                    visited[node] = True
                    queue.append(node)

# Option 1- with recursion, one function

class Graph:

    def __init__(self):
        self.graph = dict()

    def add_edge(self, key, value):
        if key not in self.graph:
            self.graph[key] = []
        self.graph[key].append(value)

    def dfs(self, source, visited=None):

        if visited == None:
            visited = {node: False for node in self.graph}
        
        print(source)
        for node in self.graph[source]:    
            if not visited[node]:
                self.dfs(node, visited)


# Option 1- with recursion, helper function

class Graph:

    def __init__(self):
        self.graph = dict()

    def add_edge(self, key, value):
        if key not in self.graph:
            self.graph[key] = []
        self.graph[key].append(value)

    def dfs_helper(self, source, visited):

        visited[source] = True
        for node in self.graph[source]:
            if visited[node] == False:
                visited[node] = True
                self.dfs_helper(node, visited)

    # This is the main function
    def dfs(self, source):

        visited = {node: False for node in self.graph}
        
        # Call helper function
        self.dfs_helper(node, visited)
