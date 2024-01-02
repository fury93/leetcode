class Solution:
    def findMatrix(self, nums: List[int]) -> 
List[List[int]]:
        d = Counter(nums)
        rows = max(d.values())
        elements = list(d.elements())
        return [elements[i::rows] for i in range
(rows)]
