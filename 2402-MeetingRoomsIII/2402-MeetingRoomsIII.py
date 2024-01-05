class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for n in nums:
            if len(sub) == 0 or sub[-1] < n:
                sub.append(n)
            else:
                pos = bisect_left(sub, n)
                sub[pos] = n

        return len(sub)
