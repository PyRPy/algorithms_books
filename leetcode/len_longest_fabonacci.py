# length of longest fibonacci subsequence
class Solution:
    def lenLongestFibSubseq(self, A):
        """ 
        type A: list[int]
        rtype: int
        """

        s = set(A)
        n = len(A)
        result = 0

        for i in range(n -1):
            for j in range(i+1, n):
                a, b = A[i], A[j]
                count = 2
                while a+b in s:
                    a, b = b, a+b 
                    count += 1
                    result = max(result, count)
        return result if result > 2 else 0

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sol = Solution()
print(A)
print(sol.lenLongestFibSubseq(A))
