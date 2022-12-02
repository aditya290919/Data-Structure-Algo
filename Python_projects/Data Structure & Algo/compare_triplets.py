def compare_triplet(a,b):

	steve = mark = 0

	for i in range(3):

		if a[i] > b[i]:

			steve+=1

		elif a[i]<b[i]:

			mark+=1

	return steve, mark

a = [2,5,3]
b = [3,6,1]

compare_triplet(a,b)
