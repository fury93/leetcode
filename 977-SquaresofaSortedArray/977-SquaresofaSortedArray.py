class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lastUniqId = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[lastUniqId]:
                lastUniqId+=1
                nums[lastUniqId] = nums[i]

        return lastUniqId+1
        
[
