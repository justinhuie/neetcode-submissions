class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        nums.sort() #[ 4, 5, 6]
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1] - 1: # If 4 does not equal 5 + 1
                return False
        return True