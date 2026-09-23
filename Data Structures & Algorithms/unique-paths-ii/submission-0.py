class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        dp = [0] * cols
        dp[cols - 1] = 1

        for r in range(rows - 1, -1, - 1):
            for c in range(cols - 1, -1, -1):
                if obstacleGrid[r][c]:
                    dp[c] = 0
                elif c + 1 < cols:
                    # In place dp[c] is the bottom and c + 1 is to the right        
                    dp[c] = dp[c] + dp[c + 1]

        return dp[0]



        
        