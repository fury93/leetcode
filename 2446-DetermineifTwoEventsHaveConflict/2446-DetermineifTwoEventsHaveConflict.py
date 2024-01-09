class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        return event1[0] <= event2[1] and event2[0] <= event1[1]
        def timeToSec(time):
            h, m = time.split(':')
            return 60 * int(h) + int(m)

        s1, e1 = timeToSec(event1[0]), timeToSec(event1[1])
        s2, e2 = timeToSec(event2[0]), timeToSec(event2[1])

        return s1 <= e2 and s2 <= e1
