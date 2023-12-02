class Solution:
    def isDecomposable(self, s: str) -> bool:
        ifTwoReserved = False
        for _, gr in groupby(s):
            ln = len(list(gr))
            if ln % 3 == 0: continue
            if ln % 3 != 2 or ifTwoReserved: return False
            ifTwoReserved = True
        return ifTwoReserved

