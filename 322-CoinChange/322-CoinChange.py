        @cache
    def coinChange2(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dp(i, amount):
    def coinChange(self, coins: List[int], amount: int) -> int:

        def dfs(i, need):
            if need == 0: return 0
        res = dfs(len(coins)-1, amount)

            if need < 0: return math.inf

            for j in range(i, -1, -1):
    # Brute-force DFS
                res = min(res, dfs(j, need - coins[j]) + 1)
            res = math.inf
class Solution:
            return res
        return res if res != math.inf else -1
[
