class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        return self.matrixBFS(grid)       

    def matrixBFS(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        max_row = len(grid)
        max_col = max_row
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        length = 0 
        queue = deque()
        visited = set()


        queue.append((0,0))

        while queue: 
            for i in range(len(queue)): # This loops for the number of items at that snapshot of queue which is the layer
                r, c = queue.popleft()
                if r == max_row -1 and c == max_col -1:
                    return length + 1 # We would only get here if the bottom left was added to the queue which can only happen if its not 1

                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c

                    if min(nr, nc) < 0 or nr >= max_row or nc >= max_col or grid[nr][nc] == 1 or (nr, nc) in visited:
                        continue

                    queue.append((nr, nc))
                    visited.add((nr, nc))
            length += 1 
        
        return -1 
            

        