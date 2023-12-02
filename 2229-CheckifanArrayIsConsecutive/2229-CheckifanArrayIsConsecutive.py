[
class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        if len(nums_set) != len(nums): return False
        minVal = min(nums)
        for n in range(minVal, minVal + len(nums)):
            if n not in nums_set: return False
        return True
