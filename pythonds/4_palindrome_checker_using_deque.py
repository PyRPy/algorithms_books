# 4_palindrome_checker_using_deque.py
from pythonds.basic import Deque 

def palchecker(sString):
    chardeque = Deque() 

    for ch in sString:
        chardeque.addRear(ch) 

    stillEqual = True 

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront() 
        last = chardeque.removeRear() 
        if first != last:
            stillEqual = False 

    return stillEqual 

print(palchecker('lsdkjfskf'))
print(palchecker('radar'))
