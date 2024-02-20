    
class Solution:
    # Top-Down 1 variant
    def deleteAndEarn(self, nums: List[int]) -> int:
        d = Counter(nums)
       
        def dp(n):
            return max(n * d[n] + dp(n-2), dp(n-1))

        return dp(max(d.keys()))
    # Top-Down 2 variant with custom cache
        @cache
            if n < 1: return 0
    def deleteAndEarn3(self, nums: List[int]) -> int:
        d = Counter(nums)
        memo = {-1 : 0, 0 : 0}
[
