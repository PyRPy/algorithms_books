# 8_topological_sorting_DAG.py
from collections import defaultdict 

# recursively find the path
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list) 
        self.V = vertices 

    def addEdge(self, u, v):
        self.graph[u].append(v) 

    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True 
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack) 
        stack.insert(0, v) 

    def topologicalSort(self):
        visited = [False] * self.V 
        stack = [] 

        for i in range(self.V):
            if visited[i] == False: 
                self.topologicalSortUtil(i, visited, stack) 
        print(stack) 

# test
g = Graph(6) 
g.addEdge(5, 2) 
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

g.topologicalSort() 

# ref: https://www.geeksforgeeks.org/topological-sorting/