class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums = sorted(filter(lambda x: x < k, nums))

        res, l, r = -1, 0, len(nums) - 1
        while l < r:
            sm = nums[l] + nums[r]
            if sm >= k:
                r -= 1
            elif sm < k:
                l += 1
                res = max(res, sm)
        return res
