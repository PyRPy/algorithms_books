# swap_nodes_in_pairs.py
# definition for singly-linked list
class ListNode:
    def __init__(self, x):
        self.val = x 
        self.next = None 

class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head 
        
        p = head 
        new_start = p.next 

        while(True):
            q = p.next 
            temp = q.next 

            q.next = p 

            if not temp or not temp.next:
                p.next = temp
                break 

            p.next = temp.next 
            p = temp 
        return new_start 

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

sol = Solution()
res = sol.swapPairs(head)
print(res.val, res.next.val, res.next.next.val, res.next.next.next.val)