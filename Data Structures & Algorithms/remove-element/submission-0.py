class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        l = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[l] = nums[i]
                counter += 1
                l += 1
        return counter
        