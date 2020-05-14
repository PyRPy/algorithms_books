# add_two_numbers_xor.py
# https://www.geeksforgeeks.org/add-two-numbers-without-using-arithmetic-operators/
# https://www.geeksforgeeks.org/python-bitwise-operators/
def Add(x, y):
    while(y != 0):
        carry = x & y 
        x = x ^ y 
        y = carry << 1 
    return x 

print(Add(15, 32))

# a = 10 = 1010 
# b =  4 = 0100 
a = 10 
b = 4 
print("a & b = ", a & b)
print("a | b = ", a | b) 
print("~ a = ", ~a) 
print("a ^ b = ", a ^ b)  # 1110 = 8 + 4 + 2
print("a >> 1 = ", a >> 1) 
print("b >> 1 = ", b >> 1)
