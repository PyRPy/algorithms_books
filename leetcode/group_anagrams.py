# group_anagrams.py
class Solution:
    def groupAnagrams(self, strs):
        solution = {}
        if len(strs) < 1:
            return strs 

        else:
            for i in range(len(strs)):
                reg = strs[i]
                regsort = "".join(sorted(reg)) 
                if regsort in solution:
                    solution[regsort].append(reg)
                else:
                    solution[regsort] = [reg]
        return solution.values()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
sol = Solution()
print(strs)
print(sol.groupAnagrams(strs))
