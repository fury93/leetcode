class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        locations = []
        for numPassengers, start, end in trips:
            locations.extend([(start, numPassengers), (end, -numPassengers)])
        locations.sort()

        for _, numPassengers in locations:
            capacity -= numPassengers
            if capacity < 0: return False

        return True

    def carPooling2(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []
        for numPassengers, start, end in trips:
            heap.extend([(start, numPassengers), (end, -numPassengers)])
        heapify(heap)
        while capacity >= 0 and heap:
            capacity -= heappop(heap)[1]

        return len(heap) == 0
[
