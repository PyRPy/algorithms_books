# gfg_linked_list_count_occurrence.py
# count the number of time a given int occurs in a linked list

# class node 
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 

    def count(self, search_for):
        current = self.head 
        count = 0 
        while current is not None:
            if current.data == search_for:
                count += 1 
            current = current.next 
        return count 

    def push(self, new_data):
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 

    def printList(self):
        temp = self.head 
        while temp:
            print(temp.data) 
            temp = temp.next 
# test 
mylist = LinkedList() 
mylist.push(1) 
mylist.push(3) 
mylist.push(1) 
mylist.push(2) 
mylist.push(1) 

# check the occurrence of a integer in a linked list
 
print("count of my list is % d" % (mylist.count(1))) 

# ref: https://www.geeksforgeeks.org/write-a-function-that-counts-the-number-of-times-a-given-int-occurs-in-a-linked-list/    
