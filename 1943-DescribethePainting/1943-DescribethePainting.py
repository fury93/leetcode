class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)

        for start, end, color in segments:
            d[start] += color
            d[end] -= color

        res, color, items = [], 0, sorted(d.items())
        for i in range(len(items)-1):
            color += items[i][1]
            if color > 0:
                res.append([items[i][0], items[i+1][0], color])
        
        return res

[
