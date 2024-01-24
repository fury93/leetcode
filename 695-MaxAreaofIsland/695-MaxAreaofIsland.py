from itertools import product
class Solution(object):
    def maxAreaOfIsland(self, grid):
        R, C, seen = len(grid), len(grid[0]), set()

        def getArea(x, y):
            area = 0
            if 0 <= x < R and 0 <= y < C and (x, y) not in seen and grid[x][y] 
== 1:
                seen.add((x, y))
                area = 1
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    area += getArea(x + dx, y + dy)

            return area
        
        return max(getArea(x, y) for x, y in product(range(R), range(C)))
[
