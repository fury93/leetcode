            ax1, ay1 = a[0]
            ax2, ay2 = a[1]
            bx1, by1 = b[0]
            bx2, by2 = b[1]

            overlapX = min(ax2, bx2) - max(ax1, bx1)
            overlapY = min(ay2, by2) - max(ay1, by1)

            if overlapX > 0 and overlapY > 0:
                minSquareSide = min(overlapX, overlapY)
                res = max(res, minSquareSide)

        return res * res
[
