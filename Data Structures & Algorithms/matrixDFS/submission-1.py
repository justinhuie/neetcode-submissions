class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        def dfs(r, c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == 1 or (r, c) in visit:
                return 0
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            visit.add((r, c))
            counts = 0 
            counts += dfs(r + 1, c)
            counts += dfs(r - 1, c)
            counts += dfs(r, c + 1)
            counts += dfs(r, c - 1)
            visit.remove((r, c))
            return counts
        return dfs(0,0)
            


  

        