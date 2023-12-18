class Solution:
    def minOperations(self, nums: List[int]) -> int:
        val = Counter(nums).values()
        return -1 if min(val) == 1 else sum((v + 2) // 3 for v 
in val)
        
