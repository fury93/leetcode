class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        return mode(b for a, b in pairwise(nums) if a == key)  
[
