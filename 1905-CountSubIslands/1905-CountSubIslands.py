            return up and down and left and right

        for r in range(rows):
            for c in range(cols):
                if grid1[r][c] == 1 and grid2[r][c] == 1 and dfs(r,c):
                    count += 1
        return count 

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

            right = dfs(r, c + 1)
            down = dfs(r + 1, c)
            left = dfs(r, c - 1)

            up = dfs(r - 1, c)
                return False

            grid2[r][c] = -1 #Doing this instead of using a visit set
        def dfs(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or grid2[r][c] <= 0):
                return True
            if grid1[r][c] == 0:
        rows, cols =  len(grid1), len(grid1[0])
        count = 0

class Solution:
    def countSubIslands2(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
[
