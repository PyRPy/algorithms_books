# gfg_binary_search_single_linked_list.py
# node 
class Node:
    def __init__(self, data):
        self.data = data    
        self.next = None 
        self.prev = None 

def newNode(x):
    temp = Node(0) 
    temp.data = x 
    temp.next = None 
    return temp 

# to find middle element 
def middle(start, last):
    if start == None:
        return None 
    slow = start 
    fast = start.next 
    while fast != last:
        fast = fast.next 
        if fast != last:
            slow = slow.next 
            fast = fast.next 
    return slow 

# binary search 
def binarySearch(head, value):
    start = head 
    last = None 
    while True:
        mid = middle(start, last) 
        if mid == None:
            return None 
        if mid.data == value:
            return mid 
        elif mid.data < value:
            start = mid.next 
        else:
            last = mid 

        if not last == None or last != start:
            break 
    return None 

# test 
head = newNode(1) 
head.next = newNode(4) 
head.next.next = newNode(7) 
head.next.next.next = newNode(8) 
head.next.next.next.next = newNode(9) 
head.next.next.next.next.next = newNode(10)

target = 7 
if binarySearch(head, target) == None:
    print("value not present\n")
else:
    print("found")

# https://www.geeksforgeeks.org/binary-search-on-singly-linked-list/