        def dfs(x, y):
            maxRightDown = (x, y)
            land[x][y] = 0
            for dx, dy in [(0, 1), (1, 0)]:
                xx, yy = x + dx, y + dy
                if xx < R and yy < C and land[xx][yy] == 1:
                    maxRightDown = max(dfs(xx, yy), maxRightDown)
            return maxRightDown 

        for x, y in itertools.product(range(R), range(C)):
            if land[x][y] == 1:
                x2, y2 = dfs(x, y)
                res.append([x, y, x2, y2])
        
        res, R, C = [], len(land), len(land[0])
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
class Solution:
[
