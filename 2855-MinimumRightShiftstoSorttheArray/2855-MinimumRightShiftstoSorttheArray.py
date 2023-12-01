[
class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        L = len(nums)
        for i in range(1, L):
            if nums[i-1] > nums[i] : break
        else:
            return 0

        for j in reversed(range(L)):
            if nums[j-1] > nums[j]: break

        return L - i if i == j and nums[-1] < nums[0] else -1   
