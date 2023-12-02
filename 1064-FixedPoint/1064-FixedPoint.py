class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        res, left, right = -1, 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == mid:
                res = mid
                right = mid - 1
            elif arr[mid] > mid: 
                right = mid - 1
            else:
                left = mid + 1
        
        return res
        
