class Solution:
    def findLongestChain(self, pairs: List[List[int]]
) -> int:
        pairs.sort(key=lambda x: x[1])
        res, prevEnd = 0, -math.inf

        for start, end in pairs:
            if start > prevEnd:
                res += 1
                prevEnd = end

        return res
[
