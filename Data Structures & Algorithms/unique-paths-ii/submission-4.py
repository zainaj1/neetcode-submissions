class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        if obstacleGrid[ROWS-1][COLS-1] == 1:
            return 0
        elif ROWS == 1 and COLS == 1:
            return 1
        
        cache = [[-1] * COLS for i in range(ROWS)]
        return self.uniquePathsMemo(obstacleGrid, cache, 0, 0)
    
    def uniquePathsMemo(self, obstacleGrid: List[List[int]], cache, r, c) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        if r >= ROWS or c >= COLS:
            return 0
        elif obstacleGrid[r][c] == 1:
            return 0
        elif r == ROWS-1 and c == COLS-1:
            return 1
        elif cache[r][c] >= 0:
            return cache[r][c]

        cache[r][c] =  self.uniquePathsMemo(obstacleGrid, cache, r + 1, c) + self.uniquePathsMemo(obstacleGrid, cache, r, c + 1)

        return cache[r][c]

    # [0,0,0],
    # [0,0,0],
    # [0,0,0]

    # [0,0,0],
    # [0,0,1],
    # [0,1,0]

        
        