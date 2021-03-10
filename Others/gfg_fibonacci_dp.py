# Program for Fibonacci numbers
# https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/

def fibonacci(n):
    f = [0, 1]
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]

# test 
print(fibonacci(10))
