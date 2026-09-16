class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Directions array to use for BFS
        # Keep visited set to keep track of (r, c)
        # nxn so dont need r and c vars
        n = len(grid)
        visited = set((0, 0))
        q = deque([(0, 0, 1)]) # r, c, length

        directions = [[0, 1], [1, 0], [0, -1], 
                        [-1, 0], [1, 1], [-1, -1], [-1, 1], [1, -1]]
        while q:
            r, c, length = q.popleft()

            # Bounds check
            if (max(r, c) == n  or min(r, c) < 0 or grid[r][c] == 1):
                continue
            
            # Check if bottom right corner
            if (r == n - 1 and c == n - 1):
                return length
            
            # Check each direction
            for dr, dc in directions:
                row = r + dr
                col = c + dc

                # If not in visited we append to q
                if ((row, col) not in visited):
                    q.append((row, col, length + 1))
                    visited.add((row, col))
        
        return -1
                
                
                
            

        