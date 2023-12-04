[
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        res, zeros, ones = math.inf, 0, sum(data)
        if not ones: return 0

        for r, n in enumerate(data, start=1):
            zeros += n == 0
            if r < ones: continue
            res = min(res, zeros)
            zeros -= data[r - ones] == 0
        
        return res



1
