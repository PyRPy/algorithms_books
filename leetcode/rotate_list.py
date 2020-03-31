# rotate_list.py
# define the single linked list
class ListNode:
    def __init__(self, x):
        self.val = x 
        self.next = None 

class Solution:
    def rotateRight(self, head, k):
        if head is None or head.next is None:
            return head 

        n = 0 
        p = head 
        while p:
            n += 1 
            p = p.next 

        k = k % n 
        if k == 0:
            return head 

        p1, p2 = head, head 
        for i in range(k):
            p2 = p2.next 
        while p2 and p2.next:
            p1 = p1.next 
            p2 = p2.next 

        output = p1.next 
        p1.next = None 
        p2.next = head 

        return output 

head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)

sol = Solution()
res = sol.rotateRight(head, 4)
print(res.val, res.next.val, res.next.next.val)
