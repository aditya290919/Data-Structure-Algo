def remove_element(nums, val):

    k = 0

    for j in range(len(nums)):
        if nums[j]!=val:
            nums[k] = nums[j]
            k+=1

    return k
