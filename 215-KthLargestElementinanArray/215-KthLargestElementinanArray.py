class Solution:
    def findKthLargest(self, nums: List[int], 
k: int) -> int:
        if len(nums) == 1: return nums[0]

        def findKthLargest(nums, k):
            pivot = random.choice(nums)
            left = [n for n in nums if n > 
pivot]
            mid = [n for n in nums if n == 
pivot]
            right = [n for n in nums if n < 
pivot]
            
