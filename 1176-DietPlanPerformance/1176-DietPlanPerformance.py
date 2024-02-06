class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        res, sm, k = 0, 0, k - 1

        for r, cal in enumerate(calories):
            sm += cal
            res -= sm < lower
            res += sm > upper
            if l < 0: continue
            sm -= calories[l]
            l = r - k
        return res
[
