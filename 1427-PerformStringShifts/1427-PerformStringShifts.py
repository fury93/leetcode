class Solution:
    def stringShift(self, s: str, shift: List[List
[int]]) -> str:
        shiftRes = 0
        for direction, amount in shift:
            if direction == 0: shiftRes += amount
            else: shiftRes -= amount
        shiftRes = shiftRes % len(s)
        
        return s[shiftRes:] + s[:shiftRes]

