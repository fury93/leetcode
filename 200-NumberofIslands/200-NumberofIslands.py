class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> 
None:
        """
        Do not return anything, modify rooms in-place 
instead.
        """
        q, R, C, E = deque(), len(rooms), len(rooms[0]), 
2147483647
        for x, y in product(range(R), range(C)):
            if rooms[x][y] == 0:
                q.append((x, y, 0))
        print(q)
        while q:
            x, y, dist = q.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)
]:
[
