class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = {}
        island_count = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])): # O(m * n)
                if grid[r][c] == "1" and not (r,c) in seen:
                    island_count += 1
                    self.dfs(grid, r, c, seen)
        return island_count
    
    # O(m * n)
    def dfs(self, grid, r, c, seen):
        if min(r, c) < 0 or r >= len(grid) or c >= len(grid[r]) or (r,c) in seen or grid[r][c] == "0":
            return
        
        seen[(r,c)] = True
        # grid[r][c] = 0

        self.dfs(grid, r + 1, c, seen)
        self.dfs(grid, r - 1, c, seen)
        self.dfs(grid, r, c + 1, seen)
        self.dfs(grid, r, c - 1, seen)
        






                    

                

        