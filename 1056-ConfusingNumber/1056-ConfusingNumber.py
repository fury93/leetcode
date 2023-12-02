class Solution:
    def confusingNumber(self, n: int) -> bool:
        d = {'0': '0', '1': '1', '6': '9', 
'8': '8', '9': '6'}
        digits = []
        for dig in str(n):
             if dig not in d:
                return False
             digits.append(d[dig])
        return int(''.join(digits[::-1])) != n
        
