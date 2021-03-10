# Program for Fibonacci numbers
# https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/

def fibonacci(n):
    if n < 0:
        print("incorrect input, positive number required.")
    elif n == 0:
        return 0 
    elif n == 1:
        return 1 
    else:
        return fibonacci(n-1) + fibonacci(n-2) 

# test 
print(fibonacci(10))
