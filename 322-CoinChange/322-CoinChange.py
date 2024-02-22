        @cache
    def coinChange3(self, coins: List[int], amount: int) -> int:
    # Brute-force DFS
                    res = min(res, dfs(remain) + 1)
            return res

        return res if (res:=dfs(amount)) != math.inf else -1

            for i in range(len(coins)):
            res = math.inf

            if need == 0: return 0
        def dfs(need):
        @cache
    def coinChange(self, coins: List[int], amount: int) -> int:
class Solution:
                remain = need - coins[i]
                if remain >= 0:
[
