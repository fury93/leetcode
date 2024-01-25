class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        R, C, seen = len(grid), len(grid[0]), set()

        def getFish(x, y):
            fish = 0
            if 0 <= x < R and 0 <= y < C and grid[x][y] > 0:
                fish += grid[x][y]
                grid[x][y] = 0
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    fish += getFish(x + dx, y + dy)

            return fish
        
        return max(getFish(x, y) for x, y in product(range(R), range(C)))
[
