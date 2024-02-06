            res.append(''.join(nums[i:i+3]))
        i += 3
        if len(nums) - 1 == i:
            last = res[-1]
            res[-1] = last[:2]
            res.append(last[2] + nums[i])
        
        for i in range(0, len(nums)-1, 3):
        res, i = [], 0
        nums = [n for n in number if n.isdigit()]
    def reformatNumber(self, number: str) -> str:
class Solution:

        return '-'.join(res)
"
