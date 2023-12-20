[
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        res, i = 0, 0
        heaters = sorted(heaters) + [math.inf]
        for house in sorted(houses):
            while heaters[i] + heaters[i+1] <= house * 2:
                i += 1
            res = max(res, abs(heaters[i] - house))
        return res


        
