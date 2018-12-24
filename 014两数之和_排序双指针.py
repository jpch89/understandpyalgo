nums = [3, 7, 10, 5, 4]


def two_sum(nums, res):
    nums.sort()
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] + nums[right] > res:
            right -= 1
        elif nums[left] + nums[right] < res:
            left += 1
        elif nums[left] + nums[right] == res:
            return left, right


print(two_sum(nums, 11))

"""
(1, 3)
"""
