                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    xx, yy = x + dx, y + dy
                    if 0 <= xx < R and 0 <= yy < C and grid[xx][yy] == 1:
                        grid[xx][yy] = 2
        
        while q and fresh > 0:
            for i in range(len(q)):
                x, y = q.popleft()
        time, q, fresh, R, C = 0, deque(), 0,  len(grid), len(grid[0])

        for x, y in product(range(R), range(C)):
            if grid[x][y] == 2:
                q.append((x, y))
            elif grid[x][y] == 1:
                fresh += 1
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
[
