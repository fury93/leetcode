class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        res, seen, l = 0, set(), 0
        for r, ch in enumerate(s):
            while ch in seen or r - l + 1 > k:
                seen.discard(s[l])
                l += 1
            seen.add(ch)
            
            if len(seen) == k: res += 1
            
        return res
