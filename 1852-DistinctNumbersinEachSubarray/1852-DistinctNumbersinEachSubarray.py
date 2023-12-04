class Solution:
    def distinctNumbers(self, nums: List[int], 
k: int) -> List[int]:
        res, window = [], defaultdict(int)
        for i, n in enumerate(nums):
            window[n] += 1
            if i + 1 < k: continue
            res.append(len(window))
            remove = nums[i-k+1]
            window[remove] -= 1
            if window[remove] == 0:
                window.pop(remove)
        return res


