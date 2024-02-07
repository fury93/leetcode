class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        def dist(point):
            pi, pj = point
            return abs(pi - rCenter) + abs(pj - cCenter)

        points = [(i, j) for i in range(rows) for j in range(cols)]
        return sorted(points, key=dist)
1
