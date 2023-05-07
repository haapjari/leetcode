# Given an array of integers nums and an integer target
# return indices of the two numbers such that they add 
# up to target.
def twoSum(nums: list[int], target: int) -> list[int]:
    i = 0
    while i < len(nums):
        j = i + 1
        while j < len(nums):
            if nums[i] + nums[j] == target:
                return [i, j]
            j +=1
        i += 1
    return []