# Need to find the maximum contiguous 
zeroes between 1 and -1 or between -1 
and 1.
class Solution:
    def captureForts(self, forts: List
[int]) -> int:
        res, ii = 0, 0
        for i, n in enumerate((forts)):
            if n:
                if forts[ii] == - n:
                    res = max(res, i - 
ii - 1)
                ii = i
        return res
        
