class Solution:
    def findMissingAndRepeatedValues(self, 
grid: List[List[int]]) -> List[int]:
        vals, dup = set(), None
        for val in chain(*grid):
            if not dup and val in vals:
                dup = val
            vals.add(val)
        
        mis = 1
        while mis in vals:
            mis += 1
                
        return [dup, mis]

