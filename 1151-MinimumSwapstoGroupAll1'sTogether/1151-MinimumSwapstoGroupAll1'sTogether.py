[
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)
        if ones == 0: return 0
        res = zeros = ones - sum(data[:ones])
        for i in range(ones, len(data)):
            zeros += data[i] == 0
            zeros -= data[i-ones] == 0
            res = min(res, zeros)
        return res

    def minSwaps2(self, data: List[int]) -> int:
        res, zeros, ones = math.inf, 0, sum(data)
        if not ones: return 0

        for r, n in enumerate(data, start=1):
            zeros += n == 0
1
