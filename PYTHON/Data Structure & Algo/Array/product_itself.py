#brute forse

def product_itself(nums):
	n = len(nums)
	ans = [1] * n

	for i in range(len(nums)):
		prod = 1

		for j in range(len(nums)):
			if j != i:
				prod *= nums[j]

		ans[j] = prod

	return ans


