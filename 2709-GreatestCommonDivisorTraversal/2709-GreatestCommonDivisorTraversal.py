        if 1 in nums:return False
        
        nums = sorted(nums,reverse=True)

        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if math.gcd(nums[i],nums[j]) > 1:
                    nums[j]*=nums[i]
                    break
            else:
        if len(nums)==1:return True
                return False
        nums = set(nums)
        return True
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
class Solution:
[
