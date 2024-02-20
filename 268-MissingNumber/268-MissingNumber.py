class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n = len(nums)
        # cur_sum = sum(nums)
        # all_sum = n * (n+1) // 2 
        
        # return all_sum - cur_sum

        res = 0
        for i, n in enumerate(nums, 1):
            res = res ^ i ^ n

        return res

    
[3,0,1]
