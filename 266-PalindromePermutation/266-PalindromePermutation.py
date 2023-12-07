    def longestNiceSubstring(self, s: str) -> 
str:
        res, symbols = '', set(s)
        for i, c in enumerate(s):
            if c.swapcase() not in symbols:
                l = self.longestNiceSubstring(s
[:i])
                r = self.longestNiceSubstring(s
[i+1:])
                return max(res, l, r, key=len)
        return s        
"
