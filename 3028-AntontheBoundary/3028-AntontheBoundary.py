class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        sm = accumulate(nums)
        return sum(1 for s in sm if s == 0)
[
