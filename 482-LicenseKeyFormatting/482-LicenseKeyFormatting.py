    
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = [ch.upper() for ch in s if ch.isalnum()]

        res, start = [], len(s) % k
        
        return '-'.join(res)
    def licenseKeyFormatting2(self, s: str, k: int) -> str:
            res.append(''.join(s[:start]))
        for i in range(start, len(s), k):
            res.append(''.join(s[i:i+k]))

        s_filtered = [ch.upper() for ch in s if ch.isalnum()]

        res = deque([])
        for i in range(len(s_filtered), 0, -k):
        if start > 0:
"
