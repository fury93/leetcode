class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        return all(val <= 2 for val in Counter(nums).values())
[
