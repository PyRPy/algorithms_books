# bfs.py
graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}

print(graph.keys())

def bfs(graph, s):
    queue = []
    queue.append(s)
    seen = set()
    seen.add(s)
    parent = {s : None}

    while len(queue) > 0:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w) 
                parent[w] = vertex 
        print(vertex)
    return parent 

parent = bfs(graph, "E")
# v = "B"
for key in parent:
    print(key, parent[key])

# while v != None:
#     print(v) 
#     v = parent[v]
