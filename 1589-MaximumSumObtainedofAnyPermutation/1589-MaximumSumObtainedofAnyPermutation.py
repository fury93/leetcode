class Solution:
    def maxSumRangeQuery(self, nums: List
[int], requests: List[List[int]]) -> int:
        freq = [0] * (len(nums) + 1)
        
        for start, end in requests:
            freq[start] += 1
            freq[end+1] -= 1
        
        freq = list(accumulate(freq))

        res = 0
        for cnt, num in zip(sorted(freq, 
[
