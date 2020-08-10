from math import log

"""
07/08/2019

This is an implementation of segment tree to solve this problem. The tree
set up follows the instruction from here:
"https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/"
We first initialize the segment tree using the information from bookings.
Then we query each the value for each leaf node. Unfortunately, this impleme-
tation didn't pass OJ (resulting in time-limit exceeded). The query is strictly
O(log(n)), but the initialization step was not O(log(n)), because for any given
range, we are not strictly confined onto one path in the tree. If the given
range is large, we might bifurcate multiple times and slow down performance.
In the discussion, there is another way of implementing segment tree and that
algorithm pass OJ. In the third part of this problem, I am going to understand
how that algorithm works.

By the way, in order to squeeze our as much performance as possible, I
implement my own stack for the initialization process.

Update:
I finally passes OJ using this implementation of segment tree. The set up is
the same as previous, but during initiation, I reduce the number of branches
we must visit. Previously, each step requires bifurcation, but now by comparing
book range to mid value of the segment range, we can eliminate left or right
path based on how mid value compares to book range's start and end. This saving
apparently is significant enough to pass the OJ. That said, the performance is
poor, with 2340 ms. The segment tree implementation in 1109_3.py clock at 832
ms. On top of that, the segtree in 1109_3.py is also more space efficient than
this one. Therefore, it's pretty clear what type of segment tree I shall imple-
ment in the future.
"""


class Solution:
    def corpFlightBookings(self, bookings, n):
        lvl = int(log(n, 2))
        if (
            2 ** lvl < n
        ):  # find tree height, given that the tree is full binary
            lvl += 1
        segtree = [0] * (2 * 2 ** lvl - 1)  # get the right size of the segtree
        for s, e, f in bookings:
            self.segTreeInit(segtree, s - 1, e - 1, f, 0, n - 1, 0)
        return [
            self.query(segtree, i, 0, n - 1, 0, len(segtree)) for i in range(n)
        ]

    def segTreeInit(self, segtree, bs, be, f, ss, se, si):
        """ Initialize segment tree info from bookings
        """
        if bs <= ss and se <= be:  # book range engulfs segtree range
            segtree[si] += f
        else:
            mid = (ss + se) // 2
            if bs > mid:  # go to right child
                self.segTreeInit(segtree, bs, be, f, mid + 1, se, 2 * si + 2)
            elif be <= mid:  # go to left child
                self.segTreeInit(segtree, bs, be, f, ss, mid, 2 * si + 1)
            else:  # go to both children
                self.segTreeInit(segtree, bs, mid, f, ss, mid, 2 * si + 1)
                self.segTreeInit(
                    segtree, mid + 1, be, f, mid + 1, se, 2 * si + 2
                )

    def query(self, segtree, q, ss, se, si, size):
        """ Find the value of each leaf node in segtree by summing up content
            of all nodes that contain the query index. O(log(n)) complexity
        """
        res = 0
        while ss <= se and si < size:
            if ss <= q <= se:
                res += segtree[si]
            mid = (ss + se) // 2
            if q <= mid:
                se = mid
                si = 2 * si + 1
            else:
                ss = mid + 1
                si = 2 * si + 2
        return res


bookings = [
    [5, 6, 45],
    [5, 6, 5],
    [1, 6, 10],
    [5, 6, 5],
    [1, 2, 15],
    [1, 2, 5],
]
n = 6
sol = Solution()
print(sol.corpFlightBookings(bookings, n))
