class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # let ans be an array []
        # we want to concatenate so it looks like [1, 2, 3] --> [1,2, 3,1, 2, 3]
        # we can use nested loops the outerloop loops for 2 times and inner length of nums
        # return ans

        ans = []
        for i in range(2):
            for j in range(len(nums)):
                ans.append(nums[j])
        return ans