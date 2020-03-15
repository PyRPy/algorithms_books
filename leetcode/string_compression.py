# string_compression.py
class Solution:
    def compresss(self, chars):
        n = len(chars)
        i, count = 0, 1

        for j in range(1, n + 1):
            if j < n and chars[j] == chars[j-1]:
                count += 1
            else:
                chars[i] = chars[j-1]
                i += 1
                if count > 1:
                    for m in str(count):
                        chars[i] = m
                        i += 1 
                count = 1

        return i

chars = ["a", "a", "b", "b", "c", "c", "c", "c"]
sol = Solution()
print(chars)
print(sol.compresss(chars))
