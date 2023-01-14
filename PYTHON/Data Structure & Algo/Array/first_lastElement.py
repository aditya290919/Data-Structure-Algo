from typing import List
class Solution:
	def searchEngine(self,nums:List[int],target:int)->List[int]:

		left = self.leftElement(nums,target)
		right = self.rightElement(nums,target)

		return left, right


	def leftElement(self,nums,target):
		left=0
		right=len(nums)-1

		while (left<=right):
			mid=(left+right)//2
			if nums[mid]==target:
				if (nums[mid]-1!=target and (mid-1)>=0 or mid==0):
					return mid

				right=mid-1

			elif nums[mid]>target:
				right=mid-1

			else:
				left=mid+1

		return -1

	def rightElement(self,nums,target):
		left=0
		right=len(nums)-1

		while (left<=right):
			mid=(left+right)//2
			if nums[mid]==target:
				if (nums[mid]+1!=target and (mid+1)<=len(nums) or mid==len(nums)-1):
					return mid

				left=mid+1

			elif nums[mid]>target:
				right=mid-1

			else:
				left=mid+1

		return -1





