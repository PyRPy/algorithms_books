# 13_recursive.py
# page 468

# factorial
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

print(fact(5))

# reverse a string
# you need a base case to return back to !
def reverse(s):
    if s == '':
        return s
    else:
        return reverse(s[1:]) + s[0]

print(reverse('hello'))

# anagrams
def anagrams(s):
    if s == "":
        return [s] 
    else:
        ans = []
        for w in anagrams(s[1:]):
            for pos in range(len(w) + 1):
                ans.append(w[:pos] + s[0] + w[pos:])
        return ans 

print(anagrams('eat'))

# fast exponentiation
def recPower(a, n):
    if n == 0:
        return 1 
    else:
        factor = recPower(a, n // 2)
        if n % 2 == 0:
            return factor 
        else:
            return factor * factor * a 

print(recPower(5, 3))

# binary search - recursive version
def recBinarySearch(x, nums, low, high):
    if low > high:
        return -1 
    mid = (low + high) // 2 
    item = nums[mid]
    if item == x:
        return mid 
    elif x < item:
        return recBinarySearch(x, nums, low, mid-1)
    else:
        return recBinarySearch(x, nums, low + 1, high)

def bisearch(x, nums):
    return recBinarySearch(x, nums, 0, len(nums)-1) 

x = 7
nums = [1, 3, 5, 7, 9, 21]
print(bisearch(x, nums))

# recursive vs iteration
def loopfib(n):
    curr = 1 
    prev = 1 
    for i in range(n-2):
        curr, prev = curr + prev, curr 
    return curr 

print(loopfib(10))

def fib(n):
    if n < 3:
        return 1 
    else:
        return fib(n-1) + fib(n-2) 

print(fib(10))
