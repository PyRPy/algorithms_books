# narray_tree_level_order_traversal.py
# defination for a node
class Node:
    def __init__(self, val, children):
        self.val = val 
        self.children = children 

class Solution:
    def levelOrder(self, root):
        if root == None:
            return []

        cur = [root]
        nex = []
        result = []

        while cur:
            tmp = []
            for n in cur:
                tmp.append(n.val)
                for c in n.children:
                    nex.append(c)
            result.append(tmp)
            cur = nex 
            nex = []

