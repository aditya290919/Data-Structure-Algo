def max_sum(arr,WindowSize):
	arraysize = len(arr)
	if (arraysize<=WindowSize):
		print('invalid input!')

		return -1

	window_sum = sum([arr[i] for i in range(WindowSize)])

	max_sum = window_sum