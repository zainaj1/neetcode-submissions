class Solution:
    """
    Note weve identified this problem to be the same as the max area of an island problem with a minor tweque
    * The area of the island is the depth of the fruit path from a starting rotten fruit to either empty cell or another rotting fruit
    * The Minimum number of minutes is just the largest island 
    * Once weve checked all the islands we need to validate if there are any freash fruits left if there are we return -1
    """
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = deque()
        depth = 0
        oranages = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    oranages += 1
        
        depth = 0 if not queue else self.bfs(queue, visited, grid)
        
        return depth if len(visited) == oranages else -1
    
    def bfs(self, queue, visited, grid):
        ROW = len(grid)
        COL = len(grid[0])
        neighbours = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        depth = -1
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                
                # grid[r][c] = 2 # We do this to prevent the algorithm from going backwords 
                for dr, dc in neighbours:
                    nr, nc = r + dr, c + dc
                    
                    if min(nr, nc) < 0 or nr >= ROW or nc >= COL or (nr, nc) in visited or grid[nr][nc] != 1:
                        continue
                    queue.append((nr, nc))
                    visited.add((nr, nc))
            
            depth += 1
            print(depth, r, c)

        return depth
    


        