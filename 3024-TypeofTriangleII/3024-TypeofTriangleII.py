class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        
        if ln == 1:
            return 'equilateral'
        elif ln == 2:
            return 'isosceles'

        return 'scalene'
        if nums[0] + nums[1] <= nums[2]:
        ln = len(set(nums))
            return 'none' 
        
[
