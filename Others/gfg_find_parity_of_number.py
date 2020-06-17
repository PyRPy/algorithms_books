# gfg_find_parity_of_number.py 
def findParity(n):
    parity = 0 
    while n: 
        parity = ~parity 
        n = n & (n - 1) 
    return parity 

# test 
n = 7 
print('the number ', n, 'in binary is ', bin(n).replace("0b", ""))
print('parity of number ', 7, '=', 'odd' if findParity(n) else 'even')

# https://www.geeksforgeeks.org/program-to-find-parity/