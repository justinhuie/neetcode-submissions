class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Create a dp table with one extra row and column to have out of bounds
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        # Loop through all of text1 and text2 iterations
        # If same character then do 1 + diagonal (has max subsequence of both subsequences)
        # Else check max right and down (max subsequence for text1 and text2 subsequences)
        # Then return the max subsequence stored in dp[0][0]
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]