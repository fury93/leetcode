class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        max_time = -1
        for h1, h2, m1, m2 in itertools.permutations(A):
            hour = h1*10 + h2
            minute = m1*10 + m2
            if hour < 24 and minute < 60:
                max_time = max(max_time, hour * 60 + minute)
        
        if max_time == -1:
            return ""
        
        return "{:02d}:{:02d}".format(max_time // 60, max_time % 60)
[
