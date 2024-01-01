class Solution:
    def maxArea(self, height: List[int]) -> int:
        res, l, r = 0, 0, len(height) - 1

        while l < r:
            volume = (r - l) * min(height[l], height[r])
            res = max(res, volume)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return res

