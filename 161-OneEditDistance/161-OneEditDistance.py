

        return isChanged or len(s) < len(t)

                    j += 1
                else:
                    i, j = i + 1, j + 1
                if len(s) == len(t):
                isChanged = True
                if isChanged: return False
            else:
                i, j = i + 1, j + 1
            if s[i] == t[j]:
        while i < len(s):
        isChanged, i, j = False, 0, 0
        
        if len(t) - len(s) > 1: return False
        
        if len(s) > len(t): return self.isOneEditDistance(t, s) 
    def isOneEditDistance(self, s: str, t: str) -> bool:
class Solution:
"
