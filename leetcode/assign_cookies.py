# assign_cookies.py
class Solution:
    def findContentChildren(self, g, s):
        cnt = 0
        i, j = len(g) - 1, len(s) - 1 
        g, s = sorted(g), sorted(s) 
        while min(i, j) >= 0:
            if g[i] <= s[j]:
                cnt += 1 
                j -= 1 
            i -= 1 
        return cnt 

g = [1, 2, 3]
s = [1, 1]
sol = Solution()
print(g, " ", s)
print(sol.findContentChildren(g, s))
