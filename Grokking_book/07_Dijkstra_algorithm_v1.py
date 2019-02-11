# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 14:13:40 2019
# Chapter 7 Dijkstra's algorithms
# page-231 Grokking algorithms book
"""

# assign the weights to edges
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

print(graph["start"]["a"])

# add the rest of the nodes and its neighbors
graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] ={}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

# start of the program
# cost table
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# hash table for storing parent nodes
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# nodes tracker
processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)
print(node)

while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print("lowest_cost_node: ", node)
print("processed : ",  processed)