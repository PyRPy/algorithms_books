# find_difference.py
class Solution:
    def findDifference(self, s, t):
        s_dict = dict()
        for x in s:
            if x in s_dict:
                s_dict[x] += 1 
            else:
                s_dict[x] = 1 

        for y in t:
            if y not in s_dict:
                return y 
            elif s_dict[y] == 0:
                return y 
            else:
                s_dict[y] -= 1

s = "abcd"
t = "dcaeb"
sol = Solution()
print(s, " ", t)
print(sol.findDifference(s, t))

