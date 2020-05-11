# 8_Dijkstras_algorithm.py
# reference code from 'grokking algorithms'
# build the graph 
graph = {}
graph["start"] = {} 
graph["start"]["a"] = 1 
graph["start"]["b"] = 2 

# print(graph["start"].keys())
# print(graph["start"]["b"])
# print("print out 'start' ", graph["start"])

graph["a"] = {} 
graph["a"]["fin"] = 1 

graph["b"] = {} 
graph["b"]["a"] = 3 
graph["b"]["fin"] = 5 

graph["fin"] = {} 

# costs table 
infinity = float("inf")
costs = {} 
costs["a"] = 1 
costs["b"] = 2 
costs["fin"] = infinity 

# parent table 
parents = {} 
parents["a"] = "start" 
parents["b"] = "start" 
parents["fin"] = None 

# marker 
processed = [] 
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lower_cost_node = None 
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost 
            lower_cost_node = node 
    return lower_cost_node

# search for the path 
node = find_lowest_cost_node(costs)
# print("find the start node: ", node)

while node is not None:
    cost = costs[node] 
    neighbors = graph[node] 
    # print("neighbors: ", neighbors)
    for n in neighbors.keys():
        new_cost = cost + neighbors[n] 
        # print("new cost: ", new_cost)
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node 
    processed.append(node) 
    # print("processed: ", processed)
    node = find_lowest_cost_node(costs) 
    # print("find lowest cost node: ", node) 
    # print("parent: ", parents)
