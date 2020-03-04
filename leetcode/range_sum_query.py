# range_sum_query.py
class NumArray:
    def __init__(self, nums):
        self.accu = [0]
        for num in nums:
            self.accu.append(self.accu[-1] + num)

    def sumRange(self, i, j):
        return self.accu[j + 1] - self.accu[i]

nums = [-2, 0, 3, -5, 2, -1]
print(nums)
sol = NumArray(nums)

print(sol.sumRange(0, 2))