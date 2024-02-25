            overlapX = min(ax2, bx2) - max(ax1, bx1)
            overlapY = min(ay2, by2) - max(ay1, by1)

            if overlapX > 0 and overlapY > 0:
                minSquareSide = min(overlapX, overlapY)
                res = max(res, minSquareSide)
        for ((ax1, ay1), (ax2, ay2)), ((bx1,·by1),·(bx2,·by2)) in combinations(coordinats, 2):
        
        coordinats = list(zip(bottomLeft, topRight))
        res = 0 # the rectange side

        return res * res

    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        return res * res

                    res = max(res, minSquareSide)
                    minSquareSide = min(overlapX, overlapY)
                overlapX = min(ax2, bx2) - max(ax1, bx1)
                overlapY = min(ay2, by2) - max(ay1, by1)

                # move to the next i-th rectangle, no more intersactions between i-th and j-th rectangles
                if overlapX < 0 and overlapY < 0: break 
                if overlapX > 0 and overlapY > 0:
[
