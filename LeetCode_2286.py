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
    def __init__(self, n: int):
        


class BookMyShow:

    def __init__(self, n: int, m: int):
        self.empty_seats = [m] * n
        self.seg_tree = SegTree(n, m)

    def gather(self, k: int, maxRow: int) -> List[int]:
        

    def scatter(self, k: int, maxRow: int) -> bool:



sol = Solution()
tests = [
    ([4,2,1,3], [[1,2],[2,3],[3,4]]),
    ([1,3,6,10,15], [[1,3]]),
    ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
]

for i, (arr, ans) in enumerate(tests):
    res = sol.minimumAbsDifference(arr)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
