class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        top = 0
        bot = rows - 1
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
        
        row = (top + bot) // 2
        left = 0
        right = cols - 1
        while left <= right:
            middle = (left + right) // 2
            if target > matrix[row][middle]:
                left = middle + 1
    
            elif target < matrix[row][middle]:
                right = middle - 1
            
            elif target == matrix[row][middle]:
                return True
        return False
            

        


        