# balanced binary tree or not
class TreeNode(object):
    def __init__(self, x):
        self.val = x 
        self.left = None 
        self.right = None 

class Solution(object):
    def isBalanced(self, root):
        """
        type root: TreeNode 
        rtype: bool 
        """

        def get_height(root):
            if root is None:
                return 0
            left_height, right_height = get_height(root.left), get_height(root.right)
            if left_height < 0  or right_height < 0 or abs(left_height - right_height) > 1:
                return -1 
            return max(left_height, right_height) + 1 
        
        return (get_height(root) >= 0)       
