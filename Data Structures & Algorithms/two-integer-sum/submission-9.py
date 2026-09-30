class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        temp = target

        for i, n in enumerate(nums):
            if (target - n) in prev:
                return [prev[target - n], i]
            else: 
                prev[n] = i

              