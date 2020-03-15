# number_of_boomerangs.py
class Solution:
    def numberOfBoomerangs(self, points):
        result = 0 

        for x1, y1 in points:
            dicts = {}

            for x2, y2 in points:
                if x1 == x2 and y1 == y2:
                    continue 

                dx = x1 - x2 
                dy = y1 - y2 
                d2 = dx * dx + dy * dy 

                if d2 in dicts:
                    result += dicts[d2]
                    dicts[d2] += 1 
                else:
                    dicts[d2] = 1 

        return result * 2 

points = [[0,0], [1,0], [2,0]]
sol = Solution()
print(sol.numberOfBoomerangs(points))
