class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # First initalize res and subset
        res = []
        subset = []

        def dfs(index):
            if index >= len(nums):
                res.append(subset.copy())
                return
            
            # Case where we include nums[index]

            subset.append(nums[index])
            dfs(index + 1)

            # Case where we dont include nums[index]
            subset.pop()
            dfs(index + 1)
        dfs(0)
        return res