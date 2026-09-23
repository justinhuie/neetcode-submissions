class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Define bottom row
        row = [1] * n
        
        # We have bottom row so no need to loop m
        for i in range(m - 1):
            newRow = [1] * n
            # We can skip m - 1 because it will always be 1
            for j in range(n - 2, -1, -1):
                # The cell is equal to R (newRow[j + 1]) + D row[j]
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        
        return row[0]