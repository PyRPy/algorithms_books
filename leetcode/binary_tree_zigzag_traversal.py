# binary_tree_zigzag_traversal.py
# definition for a binary tree node:
class TreeNode:
    def __init__(self, x):
        self.val = x 
        self.left = None 
        self.right = None 

class Solution:
    def zigzagLevelOrder(self, root):
        q, res = [(root, 1)], [] 
        if not root:
            return res 

        while q != []:
            node, level = q.pop(0) 
            if node.left != None:
                q.append((node.left, level + 1)) 
            if node.right != None:
                q.append((node.right, level + 1)) 
            if level == len(res): 
                res[level - 1].append(node.val) 
            else:
                res.append([node.val]) 

        for i in range(len(res)):
            if i % 2 == 1:
                res[i] = res[i][::-1] 
        return res 

# build a tree
#     3
# 9       20
#     15      7
node1 = TreeNode(3) 
node2 = TreeNode(9) 
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7) 

node1.left = node2 
node1.right = node3 

node3.left = node4 
node3.right = node5 

sol = Solution() 
print(sol.zigzagLevelOrder(node1)) 
