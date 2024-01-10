class Solution:
    def eraseOverlapIntervals(self, intervals: List
[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        res, prevEnd = 0, -math.inf
        
        for start, end in intervals:
[
