class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.ROW, self.COL = len(image), len(image[0])
        starting_color = image[sr][sc]
        seen = {}
        return self.dfs(image, sr, sc, starting_color, color, seen)

    def dfs(self, image, r, c, starting_color, new_color, seen):
        
        # Base case
        # 1. Colour is not the same
        # 2. Out of bounds
        if min(r, c) < 0 or r >= self.ROW or c >= self.COL or image[r][c] != starting_color or (r,c) in seen:
            return image

        # Update color
        image[r][c] = new_color
        seen[(r, c)] = True

        # Dfs 
        self.dfs(image, r + 1, c, starting_color, new_color, seen) # Right
        self.dfs(image, r - 1, c, starting_color, new_color, seen) # Left
        self.dfs(image, r, c + 1, starting_color, new_color, seen) # Up 
        self.dfs(image, r, c - 1, starting_color, new_color, seen) # Down

        return image
        
        