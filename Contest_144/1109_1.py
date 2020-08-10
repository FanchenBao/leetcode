"""
07/07/2019

An easy problem at first sight, but the naive O(n^2) method timed out. And I
couldn't find a better solution. From discussion, I leared the following
algorithm, for which the term "magic" was an understatement. The following
was the explanation I posted on one of the comments in the discussion.

In the final res array, for any two adjacent cells (indices i-1 and i),
there are only two possibilities. Either i-1 and i have been included together
within the range in the some bookings, or i-1 and i just happen to be separated
in two different bookings. If we do res[i] += res[i-1], we can take all the
flights from i-1 to i, including the flights shared by both (this is what we
want), and the flights only for i-1 but not i (this is what we don't want).
Thus, we only need to remove those flights not in i, then we have res[i].
Notice that when i-1 and i are separated, the only possibility is that i-1 is
the end of some booking and i is the start of some other booking. Therefore,
to remove the flights that are in i-1 but not in i from res[i], each time a
range ending in i-1 is encountered, res[i] -= k, where k is the flights in the
range.
"""


class Solution:
    def corpFlightBookings(self, bookings, n):
        res = [0] * n
        for s, e, f in bookings:
            res[
                s - 1
            ] += f  # each range's start automatically increment flights
            # for each range's end (excluding end of all ranges), its next
            # element must minus its flight, because the next element is not
            # included in current range
            if e < n:
                res[e] -= f
        for i in range(1, n):
            res[i] += res[i - 1]
        return res


bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
n = 5
sol = Solution()
print(sol.corpFlightBookings(bookings, n))
