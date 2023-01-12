def my_func(my_list):
	max_value= my_list[0]
	for i in range(len(my_list)):
		if my_list[i]>max_value:
			max_value=my_list[i]
	print(max_value)

