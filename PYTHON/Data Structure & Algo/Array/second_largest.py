#optimised

def second_largest(arr):
	if not arr or len(arr) < 2:
		return None

	first = second = None

	for x in arr:
		if first is None or x > first:
			if x != first:
				second = first
			first = x

		elif x != first and (second is None or x > second):
			second = x
	
	return second


	

