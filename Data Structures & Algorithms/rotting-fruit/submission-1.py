class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # n x m grid of 3 possible values
        # 0 represents empty cell
        # 1 represents fresh fruit
        # 2 represents rotten fruit
        # fresh fruit adjacent to rotten fruit also becomes rotten
        # Return min minutes must elapse for zero fresh fruits to remain

        # Run multi sourced BFS

        # Initalize q with rotten oranges
        q = deque()
        fresh = 0
        time = 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        # Initalize fresh and q
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])
        
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if (row < 0 or row == rows or col < 0 or col == cols or
                    grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1
            
            time += 1
        return time if fresh == 0 else -1
                    
                



        # Pop from q then add adjacent oranges
        # Once q is empty we can stop
        # Keep track of fresh oranges initally and if fresh return - 1

        # Nested loop to find fresh oranges and rotting oranges
        # Increment fresh by one if fresh and add rotting to queue ([r, c])

        # Loop while q and fresh is not 0
        # Then loop for range(q)
        # Get coordinates from q and have directions array
        # Check if in bounds and == 1
        # Check grid[r][c] == 2 and append row,  col to q
        # Decrement fresh then increment time by 1
        # Return time if fresh == 0 else -1
        