# Sliding Window – Maximum Sum Subarray of Size K

def max_sum_subarray(arr, k):
	window_sum = 0
	max_sum = 0
	start = 0

	for end in len(range(arr)):
		window_sum += arr[end]

		if end >= k -1:
			max_sum = max(window_sum, max_sum)
			window_sum -= arr[start]
			start += 1

	return max_sum
