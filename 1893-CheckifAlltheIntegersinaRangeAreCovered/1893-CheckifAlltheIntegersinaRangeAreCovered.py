[
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        interval = None

        for start, end in ranges:
            if end < left: continue #skip all intervals < left

            if not interval:
                if start > left: return False # don't cover diapason [left:start-1]
                interval = [start, end]
            elif interval[1] >= start-1:
                interval[1] = max(interval[1], end)
            else:
                break # have a span between interval end and next interval start
            if interval[1] >= right: return True

        return False
