def minSubArrayLen_bruteforce(nums, best):
	n = len(nums)
	best = float('inf')

	for start in range(n):
		s = 0

		for end in range(start, n):
			s += nums[end]

			if s >= target:
				best = min(best, end - start + 1)

	return 0 if best == float('inf') else best