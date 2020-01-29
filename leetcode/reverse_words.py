# reverse words in a sentence
class Solution:
    def reverseWords(self, s):
        """
        type s: str
        rtype: str
        """

        if s == "":
            return s

        ls = s.split()

        if ls == []:
            return ""
        
        result = ""
        for i in range(0, len(ls)-1):
            result += ls[len(ls)-1-i] + " "
        result += ls[0]

        return result
s = "how are you today"
sol = Solution()
print(s)
print(sol.reverseWords(s))
