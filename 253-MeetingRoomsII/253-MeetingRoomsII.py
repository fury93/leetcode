class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted(i[0] for i in intervals)
        

        while i < len(starts):

        res, curCnt, i, j = 0, 0, 0, 0
            if starts[i] < ends[j]:
                curCnt += 1
            
        ends = sorted(i[1] for i in intervals)
                res = max(res, curCnt)
                i += 1
            else:
                curCnt -= 1
                j += 1
        
        return res

