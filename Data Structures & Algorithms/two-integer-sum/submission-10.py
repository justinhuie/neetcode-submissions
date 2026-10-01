class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hashmap to map the value n to the index i
        hashmap = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in hashmap:
                return [hashmap[difference], i]
            else:
                hashmap[n] = i
              