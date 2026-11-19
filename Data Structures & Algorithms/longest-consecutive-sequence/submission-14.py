class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numSet = set(nums)
        longest = 1

        for n in numSet:
            if n - 1 in numSet:
                continue
            temp = 1
            neighbor = n + 1
            while neighbor in numSet:
                temp += 1
                neighbor += 1
            longest = max(temp, longest)
        return longest
