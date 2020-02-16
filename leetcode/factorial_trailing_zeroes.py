# factorial trailing zeroes
class Solution(object):
    def trailingZeroes(self, n):
        """
        type n: int 
        rtype: int 
        """
        result = 0
        while n != 0:
            result += n // 5
            n = n // 5
        return result 

n = 5
sol = Solution()
print(n)
print(sol.trailingZeroes(n))

def factorial(n):
    if n < 1:
        return 1

    fact = 1
    for i in range(n):
        fact *= (i + 1 )

    return fact

print(factorial(5))
print(factorial(1))
