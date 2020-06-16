# gfg_is_linked_list_circular.py
# node class 
class Node:
    def __init__(self, data):
        self.data = data    
        self.next = None 

# linked list 
class LinkedList: 
    def __init__(self):
        self.head = None 

def Circular(head):
    if head == None:
        return True 
    # next of head 
    node = head.next 
    i = 0 
    while node is not None and node is not head:
        i = i + 1 
        node = node.next 
    return node == head 

# test 
if __name__ == '__main__':
    llist = LinkedList() 
    llist.head = Node(1) 
    second = Node(2) 
    third = Node(3) 
    fourth = Node(4) 

    llist.head.next = second 
    second.next = third 
    third.next = fourth 

    if Circular(llist.head):
        print('yes')
    else:
        print('no')

    fourth.next = llist.head  # mistake '=' / '==' difficult to spot
    if Circular(llist.head):
        print('yes')
    else:
        print('no')
# https://www.geeksforgeeks.org/check-if-a-linked-list-is-circular-linked-list/