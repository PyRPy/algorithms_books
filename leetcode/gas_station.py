# gas_station.py
class Solution:
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1 

        start = 0 
        remain = 0 

        for i in range(len(gas)):
            if gas[i] + remain < cost[i]:
                start = i + 1 
                remain = 0 
            else:
                remain += gas[i] - cost[i] 

        return start 

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

sol =  Solution() 
print(sol.canCompleteCircuit(gas, cost))
