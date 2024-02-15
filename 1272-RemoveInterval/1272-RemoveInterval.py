
        return res
            if newStart < end:
                res.append([newStart, end])
            newStart = max(start, toBeRemoved[1])
            
            if start < newEnd:
                res.append([start, newEnd])
        res = []
        for start, end in intervals:
            newEnd = min(end, toBeRemoved[0])
class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
[[0,2],[3,4],[5,7]]
