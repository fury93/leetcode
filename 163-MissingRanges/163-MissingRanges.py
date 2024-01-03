[
class Solution:
    def findMissingRanges2(self, nums: List[int], lower: int, upper: int) 
-> List[List[int]]:
        res = []
        for n in chain(nums, [upper+1]):
            if lower != n:
                res.append([lower, n-1])
            lower = n + 1
        return res

    def findMissingRanges(self, nums: List[int], lower: int, upper: int) 
-> List[List[int]]:
        if not nums: return[[lower, upper]]
        
        if nums[0] != lower:
            nums.insert(0, lower-1)
        if nums[-1] != upper:
            nums.append(upper+1)
        
        res = []
        for i in range(len(nums) - 1):
            start, end = nums[i], nums[i+1]
            if start + 1 != end:
                res.append([start+1, end-1])
        
        #for start, end in zip(nums, nums[1:]):
        #    if start + 1 != end:
