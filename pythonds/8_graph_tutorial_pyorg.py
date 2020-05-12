# 8_graph_tutorial_pyorg.py 
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

print(find_path(graph, 'A', 'E'))
print(find_path(graph, 'E', 'D'))

"""
reference and code sources:
https://www.python.org/doc/essays/graphs/
https://stackoverflow.com/questions/33727149/dict-object-has-no-attribute-has-key
"""