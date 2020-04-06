# populating_next_right_pointer.py
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val 
        self.left = left 
        self.right = right 
        self.next = next 

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root and root.left and root.right:
            root.left.next = root.right 
            if root.next:
                root.right.next = root.next.left 
            self.connect(root.left) 
            self.connect(root.right) 

        return root 

# example

#         1
#     2       3
# 4      5  6     7
node4 = Node(4)
node5 = Node(5) 
node6 = Node(6) 
node7 = Node(7)
node2 = Node(2, node4, node5)
node3 = Node(3, node6, node7) 
node1 = Node(1, node2, node3)

sol = Solution() 
root = sol.connect(node1)
print(root.left.next.val) # should be 3


 
