# remove duplicates from dorted list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None 

class Solution:
    def deleteDuplicates(self, head):
        """
        type head: listnode
        rtype: listnode
        """
        current = head
        while current:
            runner = current.next
            while runner and current.val == runner.val:
                runner = runner.next 
            current.next = runner
            current = runner
        return head

node1 = ListNode(1)

node2 = ListNode(1)

node3 = ListNode(2)

node4 = ListNode(3)

node5 = ListNode(3)


node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

sol = Solution()
print(sol.deleteDuplicates(node1))



