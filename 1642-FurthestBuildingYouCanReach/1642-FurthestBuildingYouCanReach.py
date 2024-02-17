            heapq.heappush(ladder_allocations, climb)
            if len(ladder_allocations) <= ladders:
                continue
            bricks -= heapq.heappop(ladder_allocations)
            if bricks < 0:
            if climb <= 0:
                continue
            climb = heights[i + 1] - heights[i]
        for i in range(len(heights) - 1):
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladder_allocations = []
                return i
[4,2,7,6,9,14,12]
