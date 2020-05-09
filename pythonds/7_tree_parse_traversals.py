# 7_tree_parse_traversal.py
from pythonds.basic import Stack 
from pythonds.trees import BinaryTree 

def buildParseTree(fpexp):
    fplist = fpexp.split() 
    pStack = Stack() 
    eTree = BinaryTree('')
    pStack.push(eTree) 
    currentTree = eTree 

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree) 
            currentTree = currentTree.getLeftChild()
        
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i) 
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild() 

        elif i == ')':
            currentTree = pStack.pop() 
        
        elif i not in ['+', '-', '*', '/', ')']:
            try:
                currentTree.setRootVal(int(i))
                parent = pStack.pop() 
                currentTree = parent 

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i)) 
    return eTree 

pt = buildParseTree("( ( 10 + 5 ) * 3 )")
pt.postorder() 

import operator   
def evaluate(parseTree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, 
             '/': operator.truediv} 
    
    leftC = parseTree.getLeftChild() 
    rightC = parseTree.getRightChild() 

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal() 

print('the result is: ', evaluate(pt))

# traverse a tree using function or in-class function 
def preorder(tree):
    if tree:
        print(tree.getRootVal()) 
        preorder(tree.getLeftChild()) 
        preorder(tree.getRightChild()) 

print('traverse a tree - preorder: ')
preorder(pt)

def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild()) 
        postorder(tree.getRightChild()) 
        print(tree.getRootVal())  

print('traverse a tree - postorder: ')          
postorder(pt)

def postordereval(tree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, 
             '/': operator.truediv}
    res1 = None 
    res2 = None 
    if tree:
        res1 = postordereval(tree.getLeftChild())  
        res2 = postordereval(tree.getRightChild()) 
        if res1 and res2:
            return opers[tree.getRootVal()](res1, res2) 
        else:
            return tree.getRootVal() 

print('post order evaluation: ')
print(postordereval(pt))


def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild()) 
        print(tree.getRootVal()) 
        inorder(tree.getRightChild()) 

print('in order traveral: ')        
print(inorder(pt))

def printexp(tree):
    sVal = "" 
    if tree:
        sVal = '(' + printexp(tree.getLeftChild()) 
        sVal = sVal + str(tree.getRootVal()) 
        sVal = sVal + printexp(tree.getRightChild()) + ')' 
    return sVal 

print('print the expression: ')
print(printexp(pt))
    