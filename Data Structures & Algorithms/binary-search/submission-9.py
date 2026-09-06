class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Return index of target if found
        # Sorted in ascending order
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] > target:
                right = middle - 1
            if nums[middle] < target:
                left = middle + 1
            if nums[middle] == target:
                return middle
        return -1
        
        
        