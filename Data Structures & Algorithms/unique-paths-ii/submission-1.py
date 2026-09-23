class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        # Initalize cache and bottom right as 1
        dp = [0] * cols
        dp[cols - 1] = 1

        # Loop for grid
        # If we encounter a 1 then set that cell in dp to 0 since 0 valid paths
        # Else if the value is in bounds then calculate down + right (dp[c]) is down from
        # Latest row
        # Then return dp[0] which has paths from r + d
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if obstacleGrid[r][c]:
                    dp[c] = 0
                elif c + 1 < cols:
                    dp[c] = dp[c] + dp[c + 1]
        return dp[0]



        
        