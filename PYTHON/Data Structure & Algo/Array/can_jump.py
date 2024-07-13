class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farhtest = 0

        for i in range(len(nums)):
            if i>farhtest:
                return False

            farthest = max(farthest, i + nums[i])

        return True