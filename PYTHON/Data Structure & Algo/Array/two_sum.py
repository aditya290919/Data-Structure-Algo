def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        needed = target - x
        if needed in seen:
            return [nums[needed], i]
        seen[x]  = i
