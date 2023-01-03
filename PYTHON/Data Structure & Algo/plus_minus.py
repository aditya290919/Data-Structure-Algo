def plus_minus(arr):

	positive = negative = zero = 0

	for i in arr:
		if i > 0:
			positive+=1

		if i < 0:
			negative+=1

		zero+=1
		
	print(positive/len(arr))
	print(negative/len(arr))
	print(zero/len(arr))


arr = [4,2,-5,0,1,-2]
plus_minus(arr)