class Solution:
	def missingNumber(self,nums:List[int])->int:
		current_sum=sum(nums)
		n = len(nums)
		intendedSum = n*(n+1)/2
		return int(intendedSum - current_sum)