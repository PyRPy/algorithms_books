# recursion examples
def factorial(n):
    print("factorial called with n = ", str(n))
    if n == 1 or n ==0:
        print("Ending conidtin met.")
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))

# using coninuation condition
def factorial2(n):
    print("factorial called with n = ", str(n))
    if n > 1:
        return n*factorial2(n-1) # figure it out
    print("Ending condition met.")
    return 1

print(factorial2(5))

# using while loop
def factorial3(n):
    print("factrial called with n = ", str(n))
    result = 1
    while n > 1:
        result = result*n
        n = n - 1
        print("current value of n is ", str(n))
    print("Ending condition met.")
    return result

print(factorial3(5))
