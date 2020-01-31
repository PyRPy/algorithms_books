# add two numbers
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None 

class Solution:
    def addTwoNumbers(self, l1, l2):
        if l1 == None:
            return l1 

        if l2 == None:
            return l2

        carry = 0
        dummy = ListNode(0)
        p = dummy 

        while l1 and l2:
            p.next = ListNode((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) // 10
            l1 = l1.next
            l2 = l2.next 
            p = p.next 

        if l2:
            while l2:
                p.next = ListNode((l2.val + carry) % 10)
                carry = (l2.val + carry) //10
                l2 = l2.next
                p = p.next 

        if l1:
            while l1:
                p.next = ListNode((l1.val + carry) % 10)
                carry = (l1.val + carry) // 10
                l1 = l1.next
                p = p.next 
        return dummy.next 

l1 = ListNode(["2", "4", "3"])
l2 = ListNode(["5", "6", "4"])
sol = Solution()
print(l1)
print(l2)
print(sol.addTwoNumbers(l1, l2))