nums = [3, 7, 10, 5, 4]

def two_sum(nums, target):
    d = {}
    for i in range(len(nums)):
        if target - nums[i] in d:
            return nums[i], d[target - nums[i]]
        else:
            d[nums[i]] = i

print(two_sum(nums, 11))
"""
(4, 1)
"""
