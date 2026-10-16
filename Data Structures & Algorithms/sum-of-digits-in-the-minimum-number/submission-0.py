class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        nums.sort()
        
        smallest = nums[0]
        res = 0
        for digits in str(smallest):
            res += int(digits)
        
        if res % 2 == 0:
            return 1
        else:
            return 0

