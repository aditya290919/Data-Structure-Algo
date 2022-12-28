def diagonal_diff(arr):

	left_diag, right_diag = 0, 0

	i = 0
	j = 0

    # for left_diogonal_sum

	while (i<len(arr)):

		left_diag += arr[i][j]

		i +=1
		j +=1

	x = 0
	y = len(arr) - 1

	# for right_diogonal_sum
	while (x<len(arr)):

		right_diag += arr[x][y]

		x +=1
		y -=1

	return (abs(left_diag - right_diag))


arr =  [[1,2,6],
		[8,1,9],
		[5,6,7]]

diagonal_diff(arr)


	