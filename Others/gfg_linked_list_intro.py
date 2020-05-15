# gfg_linked_list_intro.py
# node class 
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 
    def printList(self):
        temp = self.head 
        while temp:
            print(temp.data) 
            temp = temp.next 

# test 
# build a linked list
mylist = LinkedList() 
mylist.head = Node(1) 
second = Node(2) 
third = Node(3) 

mylist.head.next = second 
second.next = third 

# print the list
mylist.printList()

# https://www.geeksforgeeks.org/linked-list-set-1-introduction/