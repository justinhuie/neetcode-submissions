class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # We need to initalize res and then dfs
        res = []
        def dfs(index, cur, total):
            # Base case is if total == target then append it to res
            # Another base case is if index goes over len(nums) or total > target
            if total == target:
                res.append(cur.copy())
                return
            if index >= len(nums) or total > target:
                return
            
            # Case to include nums[i]
            cur.append(nums[index])
            dfs(index, cur, total + nums[index])

            # Case to not include nums[i]
            cur.pop()
            dfs(index + 1, cur, total)
        dfs(0, [], 0)
        return res
            
        


        