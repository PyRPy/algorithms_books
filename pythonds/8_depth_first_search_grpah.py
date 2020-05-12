# 8_depth_first_search_grpah.py
# ref: https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
from collections import defaultdict 

# build a graph with dfs method
class Graph:
    # constructor 
    def __init__(self):
        self.graph = defaultdict(list) 
    
    def addEdge(self, u, v):
        self.graph[u].append(v) 

    def DFSUtil(self, v, visited):
        visited[v] = True 
        print(v) 

        for i in self.graph[v]:
            if visited == False:
                self.DFSUtil(i, visited) 

    def DFS(self):
        V = len(self.graph) 
        visited = [False] * V 

        for i in range(V):
            if visited[i] == False:
                self.DFSUtil(i, visited) 

# test code 
g = Graph()  # new graph 
g.addEdge(0,1) 
g.addEdge(0,2) 
g.addEdge(1,2) 
g.addEdge(2,0)
g.addEdge(0,1) 
g.addEdge(2,3)
g.addEdge(3,3) 

print("following is depth first search: ")
g.DFS() 

# another test
g2 = Graph()
g2.addEdge(0,1) 
g2.addEdge(0,2) 
g2.addEdge(1,3) 
g2.addEdge(1,4) 
g2.addEdge(2,4)
g2.addEdge(3,4) 
g2.addEdge(3,5)
g2.addEdge(4,5)

print("following is depth first search: ")
g2.DFS(0, 5) # make no sense ?