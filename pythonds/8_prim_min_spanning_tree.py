# 8_prim_min_spanning_tree.py
# change 'maxint' to 'maxsize' in python3
import sys 
class Graph():
    def __init__(self, vertices):
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]
                                for row in range(vertices)]
    # helper function to print MST stored in parent[] 
    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    # helper function to find vertex with min distance value
    def minKey(self, key, mstSet):
        min = sys.maxsize 
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v] 
                min_index = v 
        return min_index 

    def primMST(self):
        key = [sys.maxsize] * self.V 
        parent = [None] * self.V 
        key[0] = 0 
        mstSet = [False] * self.V 

        parent[0] = -1 
        for cout in range(self.V):
            u = self.minKey(key, mstSet) 
            mstSet[u] = True 

            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v] 
                    parent[v] = u 
        self.printMST(parent) 

g = Graph(5)

g.graph = [ [0, 2, 0, 6, 0], 
			[2, 0, 3, 8, 5], 
			[0, 3, 0, 0, 7], 
			[6, 8, 0, 0, 9], 
			[0, 5, 7, 9, 0]] 

g.primMST()

# try another example 
g2 = Graph(5) 
g2.graph = [ [0, 10, 20, 0, 0], 
			[10, 0, 30, 5, 0], 
			[20, 30, 0, 15, 6], 
			[0, 5, 15, 0, 8], 
			[0, 0, 6, 8, 0]] 
g2.primMST()

# ref: https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
