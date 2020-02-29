# ugly_number.py
class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False 
        for i in [2, 3, 5]:
            while num % i == 0:
                num /= i 
                # print(num)

        return num == 1
num = 18
sol = Solution()
print(num)
print(sol.isUgly(num))
