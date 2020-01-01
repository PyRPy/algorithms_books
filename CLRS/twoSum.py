# two sum
from itertools import combinations
def twoSum(nums, target):
    """
    type nums : list
    type target: int
    return type : list[int]
    """

    for (i, first), (j, second) in combinations(enumerate(nums), 2):
        if first + second == target:
            return [i, j]
    return None

mynumbers = [1, 3, 5, 7, 9]
mytarget = 8
print('mynumbers: ', mynumbers)
print('mytarget: ', mytarget)

print('results: ', twoSum(mynumbers, mytarget))
