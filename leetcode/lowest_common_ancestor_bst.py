# lowest common ancestor of a binary search tree
class TreeNode:
    def __init__(self, x):
        self.val = x 
        self.left = None 
        self.right = None 

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        root type: TreeNode
        p type: TreeNode 
        q type: TreeNode
        rtype: 'TreeNode'
        """
        pointer = root 

        while pointer:
            if p.val > pointer.val and q.val > point.val:
                pointer = pointer.right 
            elif p.val < pointer.val and q.val < pointer.val:
                pointer = pointer.left 
            else:
                return pointer 
                