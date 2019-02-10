#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 16:22:52 2019

chapter 6 breadth-first search
"""

# example code on page-105
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

# first version of the code
def person_is_seller(name):
    return name[-1] == 'm'


from collections import deque
search_queue = deque()
search_queue +=graph["you"]

while search_queue:
    person = search_queue.popleft()
    if person_is_seller(person):
        print(person + " is a mango seller !")
#        return True
    else:
        search_queue += graph[person]
# return False
# if you don't write a func, there is no return values...

# corrected version
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

search("you")




