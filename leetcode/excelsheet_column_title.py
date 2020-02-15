# excel sheet column title
class Solution(object):
    def convertToTitle(self, n):
        """
        type n: init 
        rtype: str
        """

        result, num = "", n 
        while num:
            result += chr((num - 1) % 26 + ord("A"))
            num = (num - 1) // 26

        return result[::-1]

n = 29
sol = Solution()
print(n)
print(sol.convertToTitle(n))
