            else:
                dp[i] = min(dp[i-1] + costs[0], dp[max(0, i-7)] + costs[1], dp[max(0, i-30)] + costs[2])
            if i in dayset:
        for i in range(1, len(dp)):
        
        dayset = set(days)
        dp = [0] * (days[-1] + 1)
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
    # Bottom-Up (not optimized)
class Solution:
[
