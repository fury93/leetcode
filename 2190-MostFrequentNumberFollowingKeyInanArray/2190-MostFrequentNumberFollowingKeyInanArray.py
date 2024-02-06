class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        res, num_str = 0, str(num)
        for i in range(len(num_str)-k+1):
            subnum = int(num_str[i:i+k])
                res += 1
        return res
            if subnum > 0 and num % subnum == 0:

2
