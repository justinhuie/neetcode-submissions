class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Search for the row which target may be in
        # Then search that row for target
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bot =  rows - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        if not (top <= bot):
            return False
        
        left = 0
        right = cols - 1
        while left <= right:
            col = (left + right) // 2
            if target > matrix[row][col]:
                left = col + 1
            elif target < matrix[row][col]:
                right = col - 1
            elif target == matrix[row][col]:
                return True
        return False


        


        