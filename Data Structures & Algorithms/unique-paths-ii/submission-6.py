class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        path_counts = [0] * (COLS + 1)
        path_counts[COLS-1] = 1
        # Add edge case where bottom right is a 1

        for r in range(ROWS-1, -1, -1):
            for c in range(COLS-1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    path_counts[c] = 0
                else:
                    path_counts[c] = path_counts[c] + path_counts[c+1]
            print(path_counts)
        return path_counts[0]
# [0,0,0],
# [0,0,0],
# [0,0,1]

# [0,0,1,0]

# [0,0,0],
# [0,0,1],
# [0,1,0]
