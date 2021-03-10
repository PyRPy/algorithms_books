# Program for Fibonacci numbers
# https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/

# array of dp
n = 10
dp = [-1 for i in range(n + 1)]


def fibonacci(n):
    if n <= 1:
        return n
    global dp 

    first = 0 
    second = 0 

    if dp[n-1] != -1:
        first = dp[n-1] 
    else:
        first = fibonacci(n-1)
    if dp[n-2] != -1:
        second = dp[n-2] 
    else:
        second = fibonacci(n-2) 
    dp[n] = first + second 

    return dp[n] # memoization   

# test 
print(fibonacci(n))
