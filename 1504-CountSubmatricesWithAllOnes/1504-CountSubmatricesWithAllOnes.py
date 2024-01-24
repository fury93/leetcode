class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List
[int]]:
        seen, R, C, curColor = set(), len(grid), len(grid[0]), grid[row][col]

        def dfs(x, y):
            if (x, y) in seen: return True
            if not (0 <= x < R and 0 <= y < C and grid[x][y] == curColor):
                return False
            seen.add((x, y))
            adjacent = 0
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                adjacent += dfs(x + dx, y + dy)
            if adjacent < 4:
                 grid[x][y] = color
               
            return True
        
        dfs(row, col)
        
        return grid
[
