

def lin_search(lst,n):

	i = 0

	while i < len(lst):

		if lst[i] == n:

			globals()['pos'] = i

			return True

		i +=1

	return False
#take this list and number as a example
lst = [3,6,2,7,8]
n = 8

if lin_search(lst,n):
	print(f'Found at {pos}')

else:
	print('Not Found')
