class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        res, d, L = 0, defaultdict(int), len(nums) - 1
        for i in range(L, -1, -1):
            for j in range(i-1, -1, -1):
                res += d[nums[i] + nums[j]]
            for k in range(L, i-1, -1):
                d[nums[k] - nums[i]] += 1
        return res
        
    # backwards
        res, d, L = 0, defaultdict(int), len(nums)
        for i in range(L):


    def countQuadruplets2(self, nums: List[int]) -> int:
            for j in range(i+1, L):
                res += d[nums[j] - nums[i]]
        return res
            for k in range(i):
                d[nums[k] + nums[i]] += 1
[
