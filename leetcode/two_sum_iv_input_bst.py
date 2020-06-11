# two_sum_iv_input_bst.py
# definitin for a binary tree node 
class TreeNode:
    def __init__(self, val = 0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 

class Solution:
    def findTarget(self, root, k):
        """
        root : TreeNode 
        k : int 
        """ 
        S = {root.val}
        stack = [root.left, root.right]

        while stack:
            node = stack.pop() 
            if node:
                if k - node.val in S:
                    return True 
                S.add(node.val) 
                stack.extend([node.left, node.right])
        return False 

# build the bst 
root = TreeNode(5)
node3 = TreeNode(3)
root.left = node3

node2 = TreeNode(2) 
node3.left = node2 

node4 = TreeNode(4) 
node3.right = node4 

node6 = TreeNode(6) 
root.right = node6 

node7 = TreeNode(7) 
node6.right = node7 

target = 9 

# test 
sol = Solution() 
print(sol.findTarget(root, target))
