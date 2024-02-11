            d[n] = f(n-1) + f(n-2)
            return d[n]
        
        return f(n)

    def fib(self, n: int) -> int:
        if n < 2: return n

        return prev2

        prev1, prev2 = 0, 1

        for i in range(2, n+1):
            cur = prev1 + prev2
            prev1, prev2 = prev2, cur
        
        def f(n):
            if n in d:
                return d[n]
2
