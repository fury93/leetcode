            return memo[n]
                points = max(n * d[n] + dp(n-2), dp(n-1))
        def dp(n):

    # Top-Down
    def deleteAndEarn(self, nums: List[int]) -> int:
        d = Counter(nums)
        memo = {-1 : 0, 0 : 0}
            if n not in memo:
                memo[n] = points

        return dp(max(d.keys()))

    # Bottom-up
    def deleteAndEarn2(self, nums: List[int]) -> int:
        if  not nums:
[
