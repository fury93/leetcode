        meetings.sort()
        rooms = [(0,i) for i in range(n)] # (availabilityTime, roomId)
        res = [0] * n
        for start, end in meetings:
            while rooms and rooms[0][0] < start:
                _, room = heappop(rooms)
                heappush(rooms, (start, room))
            release, room = heappop(rooms)
            heappush(rooms, (release + (end-start), room))
            res[room] += 1
        
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
class Solution:
        return res.index(max(res))
    
    def mostBooked2(self, n: int, meetings: List[List[int]]) -> int:
2
