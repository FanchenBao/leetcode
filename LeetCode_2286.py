# from pudb import set_trace; set_trace()
from typing import List
import math


class SegTree:
    def __init__(self, n: int, m: int):
        self.nodes = [m] * (2**(math.ceil(math.log2(n)) + 1))
        self.range_max = n - 1

    def update(self, i: int, val: int) -> None:
        self._update(i, val, 0, self.range_max, 0)

    def _update(self, i: int, val: int, rl: int, rr: int, j: int) -> None:
        if rl == rr == i:
            self.nodes[j] = val
            return
        mid = (rl + rr) // 2
        if i > mid:
            self._update(i, val, mid + 1, rr, 2 * j + 2)
        else:
            self._update(i, val, rl, mid, 2 * j + 1)
        self.nodes[j] = max(self.nodes[2 * j + 1], self.nodes[2 * j + 2])

    def query(self, lo: int, hi: int) -> int:
        return self._query(lo, hi, 0, self.range_max, 0)

    def _query(self, lo: int, hi: int, rl: int, rr: int, j: int) -> int:
        if lo == rl and hi == rr:
            return self.nodes[j]
        mid = (rl + rr) // 2
        if lo > mid:
            return self._query(lo, hi, mid + 1, rr, 2 * j + 2)
        elif hi <= mid:
            return self._query(lo, hi, rl, mid, 2 * j + 1)
        else:
            return max(
                self._query(mid + 1, hi, mid + 1, rr, 2 * j + 2),
                self._query(lo, mid, rl, mid, 2 * j + 1),
            )


class BIT:
    def __init__(self, N: int):
        """Initialize a binary indexed tree.

        :param N: The size of the range, including min and max.
        """
        # use 1-based BIT, thus array size must be one larger than the range.
        self.bit = [0] * (N + 1)

    def update(self, pos: int, delta: int) -> None:
        """Update the value at `pos` by adding `delta`.

        Also update all the other ranges that contain `pos`.

        :param pos: The position inside a range whose value needs to be
            updated. Note that this position is one less than the index
            of the self.bit array.
        :param delta: The additional value that needs to be added to
            the value at the given position, and all the other ranges
            including the given position.
        """
        # KEY POINT: BIT index is 1-based, thus its index is one larger
        # than the given position.
        i = pos + 1
        while i < len(self.bit):
            self.bit[i] += delta
            i += (i & -i)

    def query(self, max_r: int) -> int:
        """Query the sum of values in the range 0 to `max_r`.

        The meaning of "values" us defined by the `delta` parameter
        in self.update(). It is not necessarily prefix sum.

        :param max_r: The end of the range which we want to query.
        :return: Sum of values in the range 0 to `max_r`.
        """
        # KEY POINT: Bit index is 1-based, thus its index is one larger
        # than the given max range.
        i, res = max_r + 1, 0
        while i:
            res += self.bit[i]
            i -= (i & -i)
        return res



class BookMyShow:

    def __init__(self, n: int, m: int):
        self.m = m
        self.empty_seats = [m] * n
        self.seg_tree = SegTree(n, m)
        self.bit = BIT(n)
        for i in range(n):
            self.bit.update(i, m)

    def _search_gather_row(self, lo: int, hi: int, tgt: int) -> int:
        while lo < hi:
            mid = (lo + hi) // 2
            lmax = self.seg_tree.query(lo, mid)
            if lmax >= tgt:
                hi = mid
            else:
                rmax = self.seg_tree.query(mid + 1, hi)
                if rmax >= tgt:
                    lo = mid + 1
                else:
                    return -1
        return lo

    def gather(self, k: int, maxRow: int) -> List[int]:
        if maxRow == 0 and self.empty_seats[0] < k:
            return []
        idx = self._search_gather_row(0, maxRow, k)
        if idx < 0:
            return []
        r, c = idx, self.m - self.empty_seats[idx]
        self.empty_seats[idx] -= k
        self.seg_tree.update(idx, self.empty_seats[idx])
        self.bit.update(idx, -k)
        return [r, c]

    def scatter(self, k: int, maxRow: int) -> bool:
        total_empty = self.bit.query(maxRow)
        if total_empty < k:
            return False
        idx = 0
        while k:
            if self.empty_seats[idx] >= k:
                self.empty_seats[idx] -= k
                self.seg_tree.update(idx, self.empty_seats[idx])
                self.bit.update(idx, -k)
                k -= k
            else:
                tmp = self.empty_seats[idx]
                self.empty_seats[idx] = 0
                self.seg_tree.update(idx, 0)
                self.bit.update(idx, -tmp)
                k -= tmp
            idx += 1
        return True




# sol = Solution()
# tests = [
#     ([4,2,1,3], [[1,2],[2,3],[3,4]]),
#     ([1,3,6,10,15], [[1,3]]),
#     ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
# ]

# for i, (arr, ans) in enumerate(tests):
#     res = sol.minimumAbsDifference(arr)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
