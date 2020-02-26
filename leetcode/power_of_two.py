# is power of two
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False 
        while n % 2 == 0:
            n /= 2 
        return True if n == 1 else False 

    def isPowerOfTwo2(self, n:int) -> bool:
        return n > 0 and (n & (n-1)) == 0

n = 16
m = 218
sol = Solution()
print(n)
print(sol.isPowerOfTwo(n))
print(sol.isPowerOfTwo2(m))
