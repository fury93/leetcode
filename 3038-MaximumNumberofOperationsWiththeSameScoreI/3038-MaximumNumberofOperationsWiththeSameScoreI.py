class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        for i in range(0, len(nums)-1, 2):
            sm = nums[i] + nums[i+1]
            res += 1

        prev, res = None, 0
            if sm != prev: break
            if not prev:
                prev = sm
        return res
[
