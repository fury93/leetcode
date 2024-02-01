class Solution:
    def countKeyChanges(self, s: str) -> int:
        res = 0

        for j in range(1, len(s)):
            if s[j].lower() != s[j-1].lower():
                res += 1
        return res

"
