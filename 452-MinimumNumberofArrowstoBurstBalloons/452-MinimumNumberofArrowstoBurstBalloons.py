class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: p[1])
        res, prevEnd = 1, points[0][1]
        
        for start, end in points:
            if start > prevEnd:
                res += 1
                prevEnd = end
        return res
[
