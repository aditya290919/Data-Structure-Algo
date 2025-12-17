#not optimised

def second_largest(arr):
	if len(arr)>2:
		return
	a = set(arr)
	remove_max = a.remove(max(a))
	return max(remove_max)
