# simplify_path.py
class Solution:
    def simplifyPath(self, path):
        result = []
        path_list = path.split('/')
        for p in path_list:
            if p:
                if p == '..':
                    if result:
                        result.pop() 
                elif p == '.':
                    continue 
                else:
                    result.append(p)
        res = '/' + '/'.join(result)

        return res 

path = "/a/../../b/../c//.//"
print(path)
sol = Solution()
print(sol.simplifyPath(path))

                