class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        l = 0
        r = ROWS * COLS - 1
        
        while l <= r:
            mid = (l+r) // 2
            row = mid // COLS
            col = mid % COLS

            if target < matrix[row][col]:
                r = mid - 1
            elif target > matrix[row][col]:
                l = mid + 1
            else:
                return True
        
        return False


            
        