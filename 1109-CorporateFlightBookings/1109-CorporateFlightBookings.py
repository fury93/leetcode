class Solution:
    def corpFlightBookings(self, bookings: List[List
[int]], n: int) -> List[int]:
        res = [0] * n
        for first, last, seats in bookings:
            res[first-1] += seats
            if last < n:
                res[last] -= seats
        return accumulate(res)
[
