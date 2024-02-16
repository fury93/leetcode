class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        frequency = list(Counter(arr).values())
        heapify(frequency)
        while k > 0 and k >= frequency[0]:
            k -= heappop(frequency)
        return len(frequency)

[5,5,4]
