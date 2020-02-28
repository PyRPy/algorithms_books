# shortest_word_distance.py
class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        type words, word1, word2: str
        rtype: int
        """
        dist = float('inf')
        i, index1, index2 = 0, None, None 
        while i < len(words):
            if words[i] == word1:
                index1 = i 
            elif words[i] == word2:
                index2 = i 

            if index1 is not None and index2 is not None:
                dist = min(dist, abs(index1 - index2))

            i += 1

        return dist 
words = ["practice", "makes", "perfect", "coding", "makes"]
sol = Solution()
print(words)
print(sol.shortestDistance(words, "makes", "coding"))
