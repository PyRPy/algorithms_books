class Solution:
    def reverseWords(self, s):
        result = []
        a = s.split()
        
        for i in range(len(a)):
            result.append(a[i][::-1])
            
        return " ".join(result)

# test code
s = "good morning, dog"
        
sol = Solution()
sol.reverseWords(s)

print('oringinal string: ', s)
print('reversed: ', sol.reverseWords(s))

# from https://www.youtube.com/watch?v=rTCGwvpNqZQ
