class Solution:
	def max_sub_array(self,array:List[int])->int:
		current_sum=0
		max_value=array[0]

		for i in array:
			current_sum+=i
			if current_sum<0:
				current_sum=0

			max_sum=max(max_value,current_sum)

		print(max_sum)
