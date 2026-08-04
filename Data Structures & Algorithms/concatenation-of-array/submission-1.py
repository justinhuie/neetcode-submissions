class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # let ans be an []
        # loop through two times
        # append nums to ans
        ans = []
        for i in range(2):
            for j in range(len(nums)):
                ans.append(nums[j])
        return ans