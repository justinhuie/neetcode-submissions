class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numberSet = {}
        for i, n, in enumerate(nums):
            difference = target - n
            if difference in numberSet:
                return [numberSet[difference], i]
            else:
                numberSet[n] = i
                      