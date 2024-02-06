class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        res, sm, l = 0, 0, 0

        for r, cal in enumerate(calories):
            sm += cal
            res -= sm < lower
            res += sm > upper
            if r - l + 1 < k: continue
            sm -= calories[l]
            l += 1
        return res
[
