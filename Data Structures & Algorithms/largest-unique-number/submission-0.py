class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = {}
        largest = -1
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for key, value in count.items():
            if value == 1:
                largest = max(largest, key)
        
        return largest