1
class Solution:
    def findMaximalUncoveredRanges(self, n: int, ranges: List[List[int]]) -> List[List[int]]:
        if not ranges:
            return [[0, n-1]]
        
        # sort by start and merge intervals
        ranges.sort()
        merged_ranges = []
        for start, end in ranges:
            if merged_ranges and merged_ranges[-1][1] >= start:
                merged_ranges[-1][1] = max(merged_ranges[-1][1], end)
            else:
                merged_ranges.append([start, end])
          
        if merged_ranges[-1][1] != n:
            merged_ranges.append([n,n])

        res, missing_start = [], 0
        for start, end in merged_ranges:
            if missing_start != start:
                res.append([missing_start, start-1])
            missing_start = end + 1
        return res      
