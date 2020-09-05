# max_value_of_equation.py
# https://leetcode.com/problems/max-value-of-equation/
# https://github.com/kamyu104/LeetCode-Solutions/blob/master/Python/max-value-of-equation.py

import collections 
class Solution:
    def findMaxValueOfEquation(self, points, k):
        """
        points : List[List[int]]
        k : int
        return : int
        """
        result = float("-inf")
        dq = collections.deque() 
        for i, (x, y) in enumerate(points):
            while dq and points[dq[0]][0] < x - k:
                dq.popleft() 
            if dq:
                result = max(result, (points[dq[0]][1] - points[dq[0]][0]) + y + x) 
            while dq and points[dq[-1]][1] - points[dq[-1]][0] <= y - x:
                dq.pop() 
            dq.append(i) 
        return result 

# test 
points = [[1,3],[2,0],[5,10],[6,-10]]
k = 1 
sol = Solution() 
print(sol.findMaxValueOfEquation(points, k))
