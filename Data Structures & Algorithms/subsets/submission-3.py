class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # First initalize res and subset
        res = []
        subset = []
        # then initalize recursive backtracking function dfs
        def dfs(index):
            if index >= len(nums):
                res.append(subset.copy())
                return
            
            # Case where we take the decision to include nums[i]
            subset.append(nums[index])
            dfs(index + 1)

            #Case where we take the decision to not include nums[i]
            subset.pop()
            dfs(index + 1)
        dfs(0)
        return res