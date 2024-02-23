
    # Top-Down
    def coinChange2(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(need):
            if need == 0: return 0
class Solution:
    #Bottom-Up
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1 
[1,2,5]
