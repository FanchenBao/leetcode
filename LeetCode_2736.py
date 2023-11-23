# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_left, bisect_right


class MaxSegTree:
    def __init__(self, N: int) -> None:
        self.N = N
        self.tree = [0] * (2**(math.ceil(math.log(N) / math.log(2)) + 1))

    def update(self, idx: int, val: int) -> None:
        self._update(0, self.N - 1, idx, 0, val)

    def query(self, ql: int, qr: int) -> int:
        return self._query(0, self.N - 1, ql, qr, 0)

    def _update(self, rl: int, rr: int, idx: int, node: int, val: int) -> None:
        if rl == rr == idx:
            self.tree[node] = val
            return
        mid = (rl + rr) // 2
        if idx <= mid:
            self._update(rl, mid, idx, node * 2 + 1, val)
        else:
            self._update(mid + 1, rr, idx, node * 2 + 2, val)
        self.tree[node] = max(self.tree[node * 2 + 1], self.tree[node * 2 + 2])

    def _query(self, rl: int, rr: int, ql: int, qr: int, node: int) -> int:
        if rl == ql and rr == qr:
            return self.tree[node]
        mid = (rl + rr) // 2
        if qr <= mid:
            return self._query(rl, mid, ql, qr, node * 2 + 1)
        if ql > mid:
            return self._query(mid + 1, rr, ql, qr, node * 2 + 2)
        return max(
            self._query(rl, mid, ql, mid, node * 2 + 1),
            self._query(mid + 1, rr, mid + 1, qr, node * 2 + 2),
        )


class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        """
        Surprisingly, this solution passed on the first try.

        Of course, we did not solve it on our own. We use the hint a lot. The
        idea is to first sort nums1 and nums2 (aka, x and y coords) based on x,
        and then form a monotonic decreasing stack on y.

        The remaining stack is guaranteed to have increasing on x and decreasing
        on y.

        Then given a query qx and qy, we perform binary search on both, which
        leads us to an xi and yi. Since all the xs larger than qx are to the
        right of xi, and all the ys larger than qy are to the left of yi, the
        max x + y must be the max of all x + y in between xi and yi on the stack.

        To solve the problem of querying max value in a range, we use segment
        tree.

        O(NlogN + MlogN), 1399 ms, faster than 76.74%
        """
        stack = []
        for x, y in sorted(list(zip(nums1, nums2))):
            while stack and y >= stack[-1][1]:
                stack.pop()
            stack.append((x, y))
        max_seg_tree = MaxSegTree(len(stack))
        for i, (x, y) in enumerate(stack):
            max_seg_tree.update(i, x + y)
        res = []
        for qx, qy in queries:
            ql = bisect_left(stack, qx, key=lambda tup: tup[0])
            qr = bisect_right(stack, -qy, key=lambda tup: -tup[1]) - 1
            if ql > qr:
                res.append(-1)
            else:
                res.append(max_seg_tree.query(ql, qr))
        return res


sol = Solution()
tests = [
    ([4,3,1,2], [2,4,9,5], [[4,1], [1,3], [2,5]], [6,10,7]),
    ([3,2,5], [2,3,4], [[4,4], [3,2], [1,1]], [9,9,9]),
    ([2,1], [2,3], [[3,3]], [-1]),
]

for i, (nums1, nums2, queries, ans) in enumerate(tests):
    res = sol.maximumSumQueries(nums1, nums2, queries)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
