class Solution:
    def findFarmland(self, land: List[List[int]]) -> List
[List[int]]:
        res, R, C = [], len(land), len(land[0])
        
        def dfs(x, y, mx):
            if x < R and y < C and land[x][y] == 1:
                land[x][y] = 0
                for dx, dy in [(0, 1), (1, 0)]:
                    mx = max(mx, (x, y), dfs(x + dx, y + 
dy, mx))
            return mx

        for x, y in itertools.product(range(R), range(C))
:
            if land[x][y] == 1:
                x2, y2 = dfs(x, y, (x, y))
                res.append([x, y, x2, y2])
        
[
