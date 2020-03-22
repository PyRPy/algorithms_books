# add_two_numbers.y
# definition for singly-linked list

class ListNode:
    def __init__(self, x):
        self.val = x 
        self.next = None 

class Solution:
    def addTwoNumbers(self, l1, l2):
        if l1 == None:
            return l2 
        if l2 == None:
            return l1 

        dummy = ListNode(0)
        p = dummy 
        carry = 0 

        while l1 and l2:
            p.next = ListNode((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) // 10 
            l1 = l1.next 
            l2 = l2.next 
            p = p.next 

        if l2: 
            while l2:
                p.next = ListNode((l2.val + carry) % 10)
                carry = (l2.val + carry) // 10 
                l2 = l2.next 
                p = p.next 
        

        if l1: 
            while l1:
                p.next = ListNode((l1.val + carry) % 10)
                carry = (l1.val + carry) // 10 
                l1 = l1.next 
                p = p.next 

        if carry == 1:
            p.next = ListNode(1)

        return dummy.next 

l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = 3 

l2 = ListNode(5)
# l2.next = 6
# l2.next.next = 4

sol = Solution()
print(sol.addTwoNumbers(l1, l2))