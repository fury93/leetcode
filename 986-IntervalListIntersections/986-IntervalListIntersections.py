class Solution:
    def computeArea(self, ax1:int, ay1:int, ax2:int, 
ay2:int, bx1:int, by1:int, bx2:int, by2:int) -> int:
        areaA = (ax2 - ax1) * (ay2 - ay1)
        areaB = (bx2 - bx1) * (by2 - by1)

        overlapX = min(ax2, bx2) - max(ax1, bx1)
        overlapY = min(ay2, by2) - max(ay1, by1)
        
        areaOverlap = 0
        if overlapX > 0 and overlapY > 0:
            areaOverlap = overlapX * overlapY
        
        totalArea = areaA + areaB - areaOverlap

        return totalArea
