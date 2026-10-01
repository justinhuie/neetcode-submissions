class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest = 1
        neighbors = set(nums)

        for n in neighbors:
            # Check if n has left neighbor
            runningSum = 1
            if (n - 1) not in neighbors:
                while (n + 1) in neighbors:
                    runningSum += 1
                    n += 1
            longest = max(longest, runningSum)

        return longest            