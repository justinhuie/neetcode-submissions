class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for n in range(2):
            for m in range(len(nums)):
                ans.append(nums[m])
        return ans;
        