class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.s = encoding
        self.p = 0

    def next(self, n: int) -> int:
        while n > 0 and self.p < len(self.s):
            if self.s[self.p] >= n:
                self.s[self.p] -= n
                break
            else:
                n -= self.s[self.p]
                self.p += 2
        
        return self.s[self.p+1] if self.p < len(self.s) else - 1
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
