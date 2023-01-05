from typing import List
class Solution:
	def maxArea(self,length:List[int])->int:
		l = 0
		r = len(length)-1
		max_area=0

		while(l<r):
			max_area=max(max_area,min(length[l],length[r]) * (r-l))
			if (length[l]<length[r]):
				l+=1

			else:
				r-=1

		return max_area