def contains_duplicate(nums):
	seen = {}

	for i in nums:
		if i in seen:
			return True
		seen.add(i)

	return False