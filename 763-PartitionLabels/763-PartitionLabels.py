class Solution:
    # todo not working!
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        bookedRooms = []
        
        for start, end in intervals:
            if bookedRooms and bookedRooms[0] <= start:
                heapq.heappop(bookedRooms)
            heapq.heappush(bookedRooms, end)
        
        return len(bookedRooms)

    def minMeetingRooms2(self, intervals: List[List[int]]) -> int:
        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[1] for i in intervals)
        
        res, curCnt, i, j = 0, 0, 0, 0
[
