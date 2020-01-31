# climbing stairs
class Solution:
    def climbStairs(self, n):
        """
        type n: int
        rtype: int
        """

        prev, current = 0, 1
        for i in range(n):
            prev, current = current, prev + current 
        return current 

n = 5
sol = Solution()
print(n)
print(sol.climbStairs(n))