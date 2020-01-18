# two sum
from intertools import combinations

def twoSum(nums, target):
    """
    :type nums : list[int]
    :type target : int
    :rtype: list(int)
    """

    for (i, first), (j, second) in combinations(enumerate(nums), 2):
        if first + second == target:
            return [i, j]
    return None

    mylist = [1, 2, 4, 6, 7, 3]
    mytarget = 8
    print(twoSum(mylist, mytarget))
