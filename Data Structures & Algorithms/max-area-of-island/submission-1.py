class Solution:
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    area = self.calculate_island_size(r, c, grid)
                    self.max_area = self.max_area if area <= self.max_area else area
        
        return self.max_area
    
    def calculate_island_size(self, r, c, grid) -> int:
        if min(r, c) < 0 or r >= len(grid) or c >= len(grid[r]) or grid[r][c] == 0:
            return 0
        
        grid[r][c] = 0
        count = 1

        count += self.calculate_island_size(r + 1, c, grid)
        count += self.calculate_island_size(r - 1, c, grid)
        count += self.calculate_island_size(r, c + 1, grid)
        count += self.calculate_island_size(r, c - 1, grid)

        return count

        
        