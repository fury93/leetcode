        d = defaultdict(int)

        for start, end, color in segments:
            d[start] += color
            d[end] -= color

        res, color, items = [], 0, sorted(d.items())
        for i in range(len(items)-1):
            start, colorDiff, end = items[i][0], items[i][1], items[i+1][0]
            color += colorDiff
            if color > 0:
                res.append([start, end, color])
        
        return res

    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
class Solution:
[
