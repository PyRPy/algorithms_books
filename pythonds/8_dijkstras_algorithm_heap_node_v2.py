# 8_dijkstras_algorithm_heap_node.py
# ref: https://stackoverflow.com/questions/22897209/dijkstras-algorithm-in-python
import sys
import heapq

class Node:

    def __init__(self, name):
        self.name = name
        self.visited = False
        self.adjacenciesList = []
        self.predecessor = None
        self.mindistance = sys.maxsize    

    def __lt__(self, other):
        return self.mindistance < other.mindistance

class Edge:

    def __init__(self, weight, startvertex, endvertex):
        self.weight = weight
        self.startvertex = startvertex
        self.endvertex = endvertex

def calculateshortestpath(vertexlist, startvertex):
    q = []
    startvertex.mindistance = 0
    heapq.heappush(q, startvertex)

    while q:
        actualnode = heapq.heappop(q)
        for edge in actualnode.adjacenciesList:
            tempdist = edge.startvertex.mindistance + edge.weight
            if tempdist < edge.endvertex.mindistance:
                edge.endvertex.mindistance = tempdist
                edge.endvertex.predecessor = edge.startvertex
                heapq.heappush(q,edge.endvertex)

def getshortestpath(targetvertex):
    print("The value of it's minimum distance is: ",targetvertex.mindistance)
    node = targetvertex
    pathfound = []
    while node:
        pathfound.append(node.name)
        # print(node.name)
        node = node.predecessor
    return pathfound

node1 = Node("S")
node2 = Node("A")
node3 = Node("B")
node4 = Node("F")

edge1 = Edge(1,node1,node2)
edge2 = Edge(2,node1,node3)
edge3 = Edge(3,node3,node2)
edge4 = Edge(1,node2,node4)
edge5 = Edge(5,node3,node4)


node1.adjacenciesList.append(edge1)
node1.adjacenciesList.append(edge2)

node2.adjacenciesList.append(edge4)

node3.adjacenciesList.append(edge3)
node3.adjacenciesList.append(edge5)

vertexlist = (node1,node2,node3,node4)

calculateshortestpath(vertexlist,node1)

pathfound = getshortestpath(node4)
# why cannot use list.reverse()
print(pathfound[::-1])
