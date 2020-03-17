# heaters.py
class Solution:
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()
        radius = 0 
        i = 0

        for house in houses:
            while i < len(heaters) and heaters[i] < house:
                i += 1 
            if i == 0:
                radius = max(radius, heaters[i] - house)
            elif i == len(heaters):
                return max(radius, houses[i] - heaters[-1])
            else:
                radius = max(radius, min(heaters[i] - house, house - heaters[i-1]))
        return radius 

houses = [1, 2, 3]
heaters = [2]
sol = Solution()
print(houses, " ", heaters)
print(sol.findRadius(houses, heaters))
