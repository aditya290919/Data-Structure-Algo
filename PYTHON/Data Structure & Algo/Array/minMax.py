from typing import List
class Solution:
    def minMax(self,nums:List[int]):
        n=len(nums)
        
        minNum=nums[0]
        maxNum=nums[0]
        
        if n==1:
            return minNum, maxNum
        
        if nums[0]>nums[1]:
            maxNum=nums[0]
            minNum=nums[1]
            
        else:
            minNum=nums[0]
            maxNum=nums[1]
            
        for i in range(2,n):
            if nums[i]>maxNum:
                maxNum=nums[i]
                
            elif nums[i]<minNum:
                minNum=nums[i]
                
                
        return maxNum,minNum
    
    
    

            
        