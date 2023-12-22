class Solution:
    def maxScore(self, s: str) -> int:
        ones, zeros, L = sum(map(int, s)), 0, len(s)
        res = 0
        for i in range(len(s)-1):
            if s[i] == '1': ones -=1
            else: zeros +=1
            res = max(res, zeros + ones)
        return res

