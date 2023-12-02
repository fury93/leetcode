[
class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        minVal = min(nums)
        nums_set = set(nums)
        for n in range(minVal, minVal + len(nums)):
            if n not in nums:
                return False
        return True
