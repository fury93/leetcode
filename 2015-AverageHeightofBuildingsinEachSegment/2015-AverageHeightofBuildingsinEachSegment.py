class Solution:
    def averageHeightOfBuildings(self, buildings: List[List[int]]) -> List[List[int]]:
        d = defaultdict(lambda: defaultdict(int))
        for start, end, height in buildings:
            d[start][0] += height
            d[start][1] += 1
            d[end][0] -= height
            d[end][1] -= 1

        res, segmentHeight, segmentCnt, buildings = [], 0, 0, sorted(d.items())
        for i in range(len(buildings)-1):
            start, end, diffHeight, diffCnt = buildings[i][0], buildings[i+1][0], buildings[i][1][0], buildings
[i][1][1]
            segmentHeight += diffHeight
            segmentCnt += diffCnt
            if segmentCnt > 0:
                averageHeight = segmentHeight//segmentCnt
[
