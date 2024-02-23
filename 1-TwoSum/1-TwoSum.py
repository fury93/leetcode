        if n <= 2: return n

        prev1 = 1
        prev2 = 2

        for i in range(2, n):
            prev1, prev2 = prev2, prev1 + prev2
        
        return prev2
    def climbStairs2(self, n: int) -> int:
        d = {}
2
