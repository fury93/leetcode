class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        res, L = 0, len(nums)
        for i in range(L):
            for j in range(i+1, L):
                d1 = int(str(nums[i])[0])
                d2 = int(str(nums[j])[-1])
                if gcd(d1, d2) == 1:
                    res += 1

        return res
