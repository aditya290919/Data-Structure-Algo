def two_sum(nums, target):
    index_of_num = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in index_of_num:
            return [index_of_num[complement],i]



        index_of_num[num] = i

    return []