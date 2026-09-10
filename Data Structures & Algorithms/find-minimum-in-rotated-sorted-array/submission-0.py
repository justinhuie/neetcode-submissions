class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return
        minNum = nums[0]
        for i in range(len(nums)):
            if minNum > nums[i]:
                minNum = nums[i]
        return minNum
            
        