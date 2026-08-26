class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])): # O(m * n)
                if grid[r][c] == "1":
                    island_count += 1
                    self.dfs(grid, r, c)
        return island_count
    
    # O(m * n)
    def dfs(self, grid, r, c):
        if min(r, c) < 0 or r >= len(grid) or c >= len(grid[r]) or grid[r][c] == "0":
            return
        
        grid[r][c] = "0"

        self.dfs(grid, r + 1, c)
        self.dfs(grid, r - 1, c)
        self.dfs(grid, r, c + 1)
        self.dfs(grid, r, c - 1)
        






                    

                

        