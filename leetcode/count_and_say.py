# count and say
class Solution:
    def countAndSay(self, n):
        
        """
        type n: int
        retype : str
        """
        seq = "1"
        for i in range(n -1):
            seq = self.getNext(seq)
        return seq 

    def getNext(self, seq):
        i, next_seq = 0, ""
        while i < len(seq):
            count = 1
            while i < len(seq) - 1 and seq[i] == seq[i+1]:
                count += 1
                i += 1

            next_seq += str(count) + seq[i]
            i += 1
        return next_seq

sol = Solution()
n = 6
print(sol.countAndSay(n))
