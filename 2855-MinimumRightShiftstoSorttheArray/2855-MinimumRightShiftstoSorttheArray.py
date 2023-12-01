[
class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        L, i = len(nums), 0
        for i in range(1, L):
            if nums[i-1] > nums[i] : break
        for j in reversed(range(L)):
            if i == L-1: return 0

            if nums[j-1] > nums[j]: break

        return L - i if i == j and nums[-1] < nums[0] else -1   
        else:
