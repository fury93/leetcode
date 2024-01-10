class Solution:
    def eraseOverlapIntervals(self, intervals: List
[List[int]]) -> int:
        intervals.sort()
        res, prevEnd = 0, intervals[0][1]
        
[
