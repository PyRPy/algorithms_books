# reverse_string.py
class Solution:
    def reverseString(self, s):
        """
        don't return anything, modify s in-place instead 
        """

        for i in range(len(s)//2):
            s[i], s[-i-1] = s[-i-1], s[i]

s = ["h", "e", "l", "l", "o"]
sol = Solution()
print(s)
sol.reverseString(s)
print(s)