# remove linked list element
# definition for singly-linked list
class ListNode:
    def __init__(self, x):
        self.val = x 
        self.next = None 

class Solution:
    def removeElements(self, head, val):
        """
        type head: ListNode
        type val: int 
        rtype: ListNode
        """
        dummy = ListNode(float('-inf'))
        dummy.next = head 
        previous, current = dummy, dummy.next 

        while current:
            if current.val == val:
                previous.next = current.next 
            else:
                previous = current 
            current = current.next 
        return dummy.next 
        