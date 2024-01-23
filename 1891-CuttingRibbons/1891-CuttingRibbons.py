        def isEnough(cutSize, k):
            for size in ribbons:
                #if size < cutSize or k == 0: break
                k -= size // cutSize
            return False
                
        while l < r:
            m = (l + r + 1) // 2
                if k <= 0: return True

        l, r = 1, max(ribbons)
        #ribbons.sort(reverse=True)
        if sm < k: return 0
        sm = sum(ribbons)
int:
    def maxLength(self, ribbons: List[int], k: int) -> 
class Solution:
