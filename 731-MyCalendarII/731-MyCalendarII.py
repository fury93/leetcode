[
from sortedcontainers import SortedDict

class MyCalendarTwo:

    def __init__(self):
        self.d = SortedDict()

    def book(self, start: int, end: int) -> bool:
        self.d.setdefault(start, 0)
        self.d.setdefault(end, 0)
        self.d[start] += 1
        self.d[end] -= 1

        overlap = 0
        for diff in self.d.values():
            overlap += diff
            if overlap == 3:
                self.d[start] -= 1
                if not self.d[start]: self.d.pop(start)
                self.d[end] += 1
                if not self.d[end]: self.d.pop(end)
                return False
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
