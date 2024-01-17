class Solution:
    def averageHeightOfBuildings(self, buildings: List[List[int]]) -> List[List[int]]:
        d = defaultdict(lambda: defaultdict(int)) # (diffHeight, diffCnt)
        for start, end, height in buildings:
            d[start][0] += height
            d[start][1] += 1
            d[end][0] -= height
            d[end][1] -= 1

        res, segmentHeight, segmentCnt, buildings = [], 0, 0, sorted(d.items())
        for i in range(len(buildings)-1):
            start, end, diffHeight, diffCnt = buildings[i][0], buildings[i+1][0], buildings[i][1][0], buildings[i][1][1]
            segmentHeight += diffHeight
            segmentCnt += diffCnt
            if segmentCnt > 0:
                averageHeight = segmentHeight//segmentCnt
                if res and res[-1][1] == start and res[-1][2] == averageHeight:
                    res[-1][1] = end
                else:
                    res.append([start, end, averageHeight])
                # merge with previous segment if they have the same average height and is neighbours
        return res
[
