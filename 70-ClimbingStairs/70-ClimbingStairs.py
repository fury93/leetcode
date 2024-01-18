class Solution:
    def climbStairs(self, n: int) -> int:
        d = {}

        def climb(n):
            if n <= 2:
                return n
            if n not in d:
                d[n] = climb(n-1) + climb(n-2)
            return d[n]

        return climb(n)
2
