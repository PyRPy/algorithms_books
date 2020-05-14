# parirty_check.py 
# return 1 if a number has add parity 
# return 0 if a number has even parity 

def getParity(n):
    parity = 0 
    while n:
        parity = ~parity 
        n = n & (n-1) 
    return parity 

# test 
n = 13 
print("parity of number ", n, " is ", 
      "odd" if getParity(n) else "even") 

# ref: https://www.geeksforgeeks.org/program-to-find-parity/
