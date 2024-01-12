class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []
        for numPassengers, start, end in trips:
            heap.extend([(start, numPassengers), (end, -numPassengers)])
        heapify(heap)
        while capacity >= 0 and heap:
            capacity -= heappop(heap)[1]

        return len(heap) == 0
[
