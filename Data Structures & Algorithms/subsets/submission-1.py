class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Initalize global variables
        res = []
        subset = []

        # dfs function
        def dfs(i):
            # base case
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # decision to include nums[i]
            subset.append(nums[i])
            # recursive call
            dfs(i + 1)

            # decision to not include nums[i]
            subset.pop()
            # recursive call
            dfs(i + 1)
        
        dfs(0)
        return res