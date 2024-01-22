class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)

        while len(sticks) > 1:
            cost = heappop(sticks) + heappop(sticks)
            heappush(sticks, cost)
            res += cost
            
        return res
        res = 0

