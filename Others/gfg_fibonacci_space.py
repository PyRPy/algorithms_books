# Program for Fibonacci numbers
# https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/

# Space Optimisataion
def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("wrong input")
    elif n == 0:
        return a 
    elif n == 1:
        return b 
    else:
        for i in range(2, n+1):
             c = a + b 
             a = b 
             b = c 
        return b 

# test 
print(fibonacci(9))
