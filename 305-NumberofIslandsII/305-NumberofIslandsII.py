    def union(self, x, y):

        return self.root[x]
        self.root[x] = self.find(self.root[x])
            return x
        if x == self.root[x]:
    def find(self, x):

        self.rank = dict()
        self.cnt = 0
class UnionFind:
    def __init__(self):
        self.root = dict()
            res.append(ds.getCnt())
                    
        return res


            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                xx, yy = x + dx, y + dy
                if ds.isExist((xx, yy)):
                    ds.union((xx, yy), (x, y))
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        res, ds = [], UnionFind()
        for x, y in positions:
            ds.add((x, y))
3
