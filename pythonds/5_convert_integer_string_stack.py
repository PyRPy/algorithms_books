# 5_convert_integer_string_stack.py
from pythonds.basic import Stack 

rStack = Stack() 

def toStr(n, base):
    convertString = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            rStack.push(convertString[n]) 
        else:
            rStack.push(convertString[n % base]) 
        n = n // base 
    res = "" 
    
    while not rStack.isEmpty():
        res = res + str(rStack.pop()) 
    
    return res 

print(toStr(1453, 16)) 
