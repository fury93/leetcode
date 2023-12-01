class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        res, L = 0, len(nums)
        for i in range(L-1):
            for j in range(i+1, L):
                if abs(nums[i]-nums[j]) <= min(nums[i], nums[j]):
                    res = max(res, nums[i] ^ nums[j])
        return res
        
