class Solution:
    def floodFill(self, image: List[List[int]], sr: 
int, sc: int, newColor: int) -> List[List[int]]:
        R, C, color = len(image), len(image[0]), 
image[sr][sc]

        def dfs(x, y):
            if image[x][y] != color: return
            image[x][y] = newColor
            for dx, dy in [(1, 0), (-1, 0), (0, 1), 
(0, -1)]:
                xx, yy = x + dx, y + dy
                if 0 <= xx < R and 0 <= yy < C and 
image[xx][yy] == color:
                    dfs(xx, yy)
        
        if color != newColor:
[
