# 8_graph_simple_example.py
# code is from book 'grokking algorithms - chapter 6' 
from collections import deque 

# build a graph of you and others
graph = {} 
graph["you"] = ["alice", "bob", "claire"]

graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = [] 
graph["peggy"] = [] 
graph["thom"] = [] 
graph["jonny"] = [] 


# search the name

def search(name):
    search_queue = deque() 
    search_queue += graph["you"]
    searched = [] 
    while search_queue:
        person = search_queue.popleft() 
        # print('popleft: ', person) 
        if not person in searched:
            if person == name:
                print(name + " is found!") 
                return True 
            else:
                search_queue += graph[person] 
                searched.append(person) 
    return False 

# test the search
print(graph["you"])
print(search("peggy"))
print(search('thom'))
print(search('jim'))
