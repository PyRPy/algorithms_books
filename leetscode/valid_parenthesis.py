class Solution:
    def isValid(self, _str):
        d = {')' : '(', '}' : '{', ']' : '['}

        stack = []
        for s in _str:
            if s in d:
                if stack and stack[-1] == d[s]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s)
        return not stack

test_string = "()[]{}"
sol = Solution()
print('test string valid : ', sol.isValid(test_string))
# ref https://zhuanlan.zhihu.com/p/90768580
