class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        start = 0
        for i in range(1, len(nums) - k + 1):
            print(i)
            for j in range(k):
                if nums[start+j] > nums[i+j]: break
                if nums[start+j] < nums[i+j]:
                    start = i
                    break
        
        return nums[start:start+k]
