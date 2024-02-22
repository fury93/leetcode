class Solution:
    def maxSpending(self, A: List[List[int]]) -> int:
        return sum(d * a for d,a in enumerate(sorted(a for r in A for a in r), 1))  
[
