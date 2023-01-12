def max_sum(arr,WindowSize):
	arraysize = len(arr)
	if (arraysize<=WindowSize):
		print('invalid input!')

		return -1

	window_sum = sum([arr[i] for i in range(WindowSize)])

	max_sum = window_sum

	for i in range(arraysize-WindowSize):
		window_sum=WindowSize-arr[i]+arr[i+k]
		max_sum=max(window_sum,max_sum)

	return max_sum
	

