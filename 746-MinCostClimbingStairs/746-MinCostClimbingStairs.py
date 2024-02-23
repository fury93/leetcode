
        return dp(len(cost))
            one = dp(n-1) + cost[n-1]
            two = dp(n-2) + cost[n-2]
            return min(one, two)
    # Top-down
    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        L = len(cost)
        for i in range(2, L):
            cost[i] = min(cost[i-1], cost[i-2]) + cost[i]
            if n <= 1: return 0
        def dp(n):
        @cache
    def minCostClimbingStairs(self, cost: List[int]) -> int:
    # Bottom-up
class Solution:
[
