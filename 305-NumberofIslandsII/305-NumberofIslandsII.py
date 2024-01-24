        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
            return x
    def find(self, x):
        if x == self.root[x]:
        self.cnt = 0

        self.root = dict()
        self.rank = dict()
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        res, ds = [], UnionFind()
        for x, y in positions:
            ds.add((x, y))
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                xx, yy = x + dx, y + dy
                if ds.isExist((xx, yy)):
                    ds.union((xx, yy), (x, y))
            res.append(ds.getCnt())
                    
        return res


class UnionFind:
    def __init__(self):
3
