class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        
        def dfs(index):
            if index >= len(nums):
                res.append(subset.copy())
                return
            
            # Choice 1: Choice to add n
            subset.append(nums[index])
            dfs(index + 1)

            # Choice 2: Exclude n
            subset.pop()
            dfs(index + 1)
        
        dfs(0)
        return res
        
