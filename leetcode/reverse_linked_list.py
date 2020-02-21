# reverse linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None 

class Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        dummy = ListNode(float("-inf"))
        while head:
            dummy.next, head.next, head = head, dummy.next, head.next 
        return dummy.next 
    