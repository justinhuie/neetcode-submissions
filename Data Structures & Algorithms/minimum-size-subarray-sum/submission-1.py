class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        length = len(nums) + 1
        L  = 0

        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                total -= nums[L]
                length = min(length, R - L + 1)
                L += 1
        
        return 0 if length == len(nums) + 1 else length

        