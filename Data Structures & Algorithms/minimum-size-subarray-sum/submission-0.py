class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        length = len(nums) + 1
        l = 0
        
        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                length = min(length, r - l + 1)
                total -= nums[l]
                l += 1
        
        if length == len(nums) + 1:
            return 0
        else:
            return length

        