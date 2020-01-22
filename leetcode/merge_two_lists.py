# merge two sorted lists
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        type l1 : ListNode
        type l2 : ListNode
        rtype: ListNode
        """

        curr = dummy = ListNode(0)
        l1 = l2 = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2

        return dummy.next

if __name__ == "__main__":

    l1 = ListNode([0, 3, 7])
    l2 = ListNode([4, 7, 9])

    sol = Solution()
    print(l1, l2)
    print(unlist(sol.mergeTwoLists(l1, l2)))
