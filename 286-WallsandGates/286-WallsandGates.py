class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        q, R, C, E = deque(), len(rooms), len(rooms[0]), 2147483647
        
            if rooms[x][y] == 0:
                q.append((x, y, 0))
        
            x, y, dist = q.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C and rooms[nx][ny] == E:
                    rooms[nx][ny] = dist + 1
        for x, y in product(range(R), range(C)):
        while q:
                    q.append((nx, ny, dist + 1))
[
