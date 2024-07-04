from typing import List
class Solution:
	def missingNumber(self,nums:List[int])->int:
		current_sum=sum(nums)
		n = len(nums)
		intendedSum = n*(n+1)/2
		return int(intendedSum - current_sum)


s = Solution()
answer=s.missingNumber([3,1,0])
print(answer)