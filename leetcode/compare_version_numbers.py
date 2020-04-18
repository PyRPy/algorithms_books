# compare_version_numbers.py
# if v1 > v2 return 1
# if v1 < v2 return -1
# otherwise return 0

class Solution:
    def compareVersion(self, version1, version2):
        version1 = version1.split('.')
        version2 = version2.split('.')

        n = max(len(version1), len(version2)) 
        i = 0  
        
        for i in range(n):
            v1 = int(version1[i]) if i < len(version1) else None 
            v2 = int(version2[i]) if i < len(version2) else None 
            if not v2 and v1:
                return 1 
            elif not v1 and v2:
                return -1 
            elif v1 and v2:
                if v1 > v2:
                    return 1 
                elif v1 < v2:
                    return -1 

        return 0 

version1 = "0.1"
version2 = "1.1.1" 
sol = Solution() 
print(sol.compareVersion(version1, version2)) 
