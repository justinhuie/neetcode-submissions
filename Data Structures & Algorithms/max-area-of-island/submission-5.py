class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Grid made of integer 1 and 0s
        # We can DFS and check adjacent directions
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        area = 0


        def dfs(r, c):
            # Base case
            if (r < 0 or r == rows or c < 0 or c == cols or
                grid[r][c] == 0 or (r, c) in visited):
                    return 0

            visited.add((r, c))

            # Recursive Call
            return (1 + dfs(r + 1, c) +
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1))

        for r in range(rows):
            for c in range(cols):
                area = max(area, dfs(r, c))
        return area