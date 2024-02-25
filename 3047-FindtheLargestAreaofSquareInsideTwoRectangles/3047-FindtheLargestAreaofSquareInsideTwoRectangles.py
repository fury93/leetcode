                bx2, by2 = coordinats[j][1] #b[1]
                overlapX = min(ax2, bx2) - max(ax1, bx1)
                bx1, by1 = coordinats[j][0] #b[0]
                overlapY = min(ay2, by2) - max(ay1, by1)
                #print(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
                ax2, ay2 = coordinats[i][1] #a[1]
                #print(overlapX, overlapY)
                ax1, ay1 = coordinats[i][0] #a[0]
        #for a, b in pairwise(coordinats):
                if overlapX > 0 and overlapY > 0:
                if overlapX < 0 and overlapY < 0: break # mote to the next i-th rectangle
                    minSquareSide = min(overlapX, overlapY)
                    res = max(res, minSquareSide)

        return res * res
            for j in range(i + 1, len(coordinats)):
[
