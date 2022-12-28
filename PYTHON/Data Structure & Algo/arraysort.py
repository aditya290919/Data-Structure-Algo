def my_func(my_list):
	for i in range(len(my_list)):
		for j in range(len(my_list)-1,0,-1):

			if my_list[j]<my_list[j-1]:
				a = my_list[j]
				my_list[j]= my_list[j-1]
				my_list[j-1]=a



	print(my_list)







