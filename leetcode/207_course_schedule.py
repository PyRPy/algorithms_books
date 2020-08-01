# 207_course_schedule.py
import collections
class Solution:
    def canFinish(self, N, prerequisites):
        graph = collections.defaultdict(list)
        indegrees = collections.defaultdict(int) 
        for u, v in prerequisites:
            graph[v].append(u) 
            indegrees[u] += 1 
        for i in range(N):
            zeroDegree = False
            for j in range(N):
                if indegrees[j] == 0:
                    zeroDegree = True 
                    break 
        if not zeroDegree:
            return False 
        indegrees[j] = -1 
        for node in graph[j]:
            indegrees[node] -= 1 
        return True 
# test 
N = 2
prerequisites = [[1,0],[0,1]]
sol = Solution() 
print(sol.canFinish(N, prerequisites))

# https://blog.csdn.net/fuxuemingzhu/article/details/82951771
# https://leetcode.com/problems/course-schedule/