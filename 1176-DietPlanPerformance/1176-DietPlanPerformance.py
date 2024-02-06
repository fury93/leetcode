class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        res, sm, k = 0, 0, k - 1

        for r, cal in enumerate(calories):
            sm += cal
            res -= sm < lower
            res += sm > upper
            if r - k < 0: continue
            sm -= calories[r - k]
        return res
[
