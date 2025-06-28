"""
Approach:
Use a nested for loop.
Iterate through the integers in the outer loop and find the integer that adds up to the target number in the inner loop.
"""

# 1451ms solution - O(n^2)

def twoSum(self, nums, target):
    for i in range(len(nums)):
        to_find = target - nums[i]
        for j in range(i+1, len(nums)):
            if nums[j] == to_find:
                return [i, j]


"""
Approach:
Use a hashmap of (value:idex) pairs. The hashmap is initially empty.
Iterate through the integers and find the difference between the integer and the target integer.
If the difference does not exist as a key in the hashmap, add the integer in the hashmap as a (value:index) pair.
If the difference does exist as a key in the hashmap, return the value of that key and the index of the current integer.
"""

# 0ms solution - O(n)

def twoSum(self, nums, target):
    checked = {}  # val : index
    for i, n in enumerate(nums):
        diff = target - n
        if diff in checked:
            return [checked[diff], i]
        checked[n] = i
    return
