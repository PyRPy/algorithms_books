# length of last word
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        count = 0
        local_count = 0

        for i in range(len(s)):
            if s[i] == ' ':
                local_count = 0
            else:
                local_count += 1
                count = local_count
        return count

sol = Solution()
s = 'how are you today'
print(s)
print(sol.lengthOfLastWord(s))
