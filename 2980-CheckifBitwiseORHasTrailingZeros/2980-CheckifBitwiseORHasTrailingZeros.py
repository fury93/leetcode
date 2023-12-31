class Solution:
    def hasTrailingZeros(self, nums: List
[int]) -> bool:
        isEvenBefore = False
        for n in nums:
            if not n & 1:
                if isEvenBefore: return True
                isEvenBefore = True
        return False
        
