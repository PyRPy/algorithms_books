# 8_graph_tutorial_pyorg.py 
from collections import deque
graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

def find_path(graph, start, end, path=[]):
    path = path + [start] 
    if start == end:
        return path 
    # if not graph.has_key(start):
    if start not in graph:
        return None 
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath 
    return None 

def find_all_paths(graph, start, end, path=[]):
    path = path + [start] 
    if start == end:
        return [path] 
    if start not in graph:
        return [] 
    paths = [] 

    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath) 
    return paths 

def find_shortest_path(graph, start, end, path=[]):
    path = path + [start] 
    if start == end:
        return path 
    if start not in graph:
        return None 
    shortest = None 
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path) 
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath 
    return shortest 

def find_shortest_path2(graph, start, end):
    dist = {start:[start]} 
    q = deque(start) 
    while len(q):
        at = q.popleft() 
        for next in graph[at]:
            if next not in dist:
                dist[next] = [dist[at], next] 
                q.append(next) 
    return dist.get(end) 



print(find_path(graph, 'A', 'E'))
print(find_path(graph, 'E', 'D'))
print(find_all_paths(graph, 'A', 'D'))
print(find_shortest_path(graph, 'A', 'D'))
print(find_shortest_path2(graph, 'A', 'D')) # output format needs attention
"""
reference and code sources:
https://www.python.org/doc/essays/graphs/
https://stackoverflow.com/questions/33727149/dict-object-has-no-attribute-has-key
"""