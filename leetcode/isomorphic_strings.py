# isomorphic strings
class Solution:
    def isIsomorphic(self, s, t):
        """
        type s: str 
        type t: str 
        rtype: bool 
        """

        if len(s) != len(t):
            return False 

        return self.halfIsom(s, t) and self.halfIsom(t, s)

    def halfIsom(self, s, t):
        lookup = {}
        for i in range(len(s)):
            if s[i] not in lookup:
                lookup[s[i]] = t[i]
            elif lookup[s[i]] != t[i]:
                return False
        return True 

# example
s = "sea"
t = "tea"
sol = Solution()
print(s)
print(t)
print(sol.isIsomorphic(s, t))
