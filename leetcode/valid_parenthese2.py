# valid parenthesis
class Solution:
    def isValid(self, s):
        stack = []
        lookup = {"(" : ")", "{" : "}", "[" : "]"}
        for parenthese in s:
            if parenthese in lookup:
                stack.append(parenthese)
                # print(stack)
            elif len(stack) == 0 or lookup[stack.pop()] !=parenthese:
                # print(stack)
                return False

        return len(stack) == 0
s = "[{[]}]"
sol = Solution()
print("original string: ", s)
print("is the parenthese valid: ", sol.isValid(s))
