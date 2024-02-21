            addRight = (nums[r] * mul[n]) + dp(n+1, l, r-1)
            return max(addLeft, addRight)
            addLeft = (nums[l] * mul[n]) + dp(n+1, l+1, r)

        return dp(0, 0, len(nums)-1)
            if n == len(mul): return 0
        def dp(n, l, r):
        @cache
    def maximumScore(self, nums: List[int], mul: List[int]) -> int:
class Solution:
[
