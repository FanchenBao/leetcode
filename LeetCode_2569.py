# from pudb import set_trace; set_trace()
from typing import List
import math
import numpy as np
from collections import defaultdict


class Solution1:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        """Numpy cheating solution works! Surprise surprise.

        9652 ms, faster than 5.04% 
        """
        nums1 = np.array(nums1)
        nums2 = np.array(nums2)
        res = []
        for q, a, b in queries:
            if q == 1:
                nums1[a:b + 1] ^= np.ones(b - a + 1, dtype=int)
            elif q == 2:
                nums2 += nums1 * a
            else:
                res.append(np.sum(nums2))
        return res


class Solution2:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        """Use lazy propagation of a segment tree.

        3269 ms, faster than 33.88%
        """
        # segment tree. Use defaultdict avoids the hassel of computing the size
        # of the array.
        tree = defaultdict(int)
        lazy = defaultdict(int)  # for lazy propogation
        N = len(nums1)


        def init_tree(idx: int, ss: int, se: int) -> int:
            """Find the total number of 1s in nums at each segment.
            """
            if ss > se:
                return 0
            if ss == se:
                tree[idx] = nums1[ss]
            else:
                mid = (ss + se) // 2
                tree[idx] = init_tree(2 * idx + 1, ss, mid) + init_tree(2 * idx + 2, mid + 1, se)
            return tree[idx]


        def update(idx: int, ss: int, se: int, us: int, ue: int) -> None:
            if lazy[idx]:
                # the current segment needs to be toggled
                # The next line is the key step, which obtains the total number
                # of 1s in the segment after everything within is toggled.
                # Basically, if there are k 1s initially in a range of length L,
                # after toggle, the number of ones is L - k
                tree[idx] = se - ss + 1 - tree[idx]
                # propagate the toggle to children
                lazy[2 * idx + 1] ^= 1
                lazy[2 * idx + 2] ^= 1
                # reset the flag for the toggle of the current node
                lazy[idx] = 0

            if ss > se or us > se or ue < ss:
                return

            if ss >= us and se <= ue:
                # toggle again, but this time it is not due to a previously set
                # lazy flag, but the current need to toggle
                tree[idx] = se - ss + 1 - tree[idx]
                lazy[2 * idx + 1] ^= 1
                lazy[2 * idx + 2] ^= 1
            else:
                mid = (ss + se) // 2
                update(2 * idx + 1, ss, mid, us, ue)
                update(2 * idx + 2, mid + 1, se, us, ue)
                tree[idx] = tree[2 * idx + 1] + tree[2 * idx + 2]


        def query(idx: int, ss: int, se: int, qs: int, qe: int) -> int:
            if lazy[idx]:
                # If there is any left over toggle that hasn't been done, do it
                # here and propagate it further down.
                tree[idx] = se - ss + 1 - tree[idx]
                lazy[2 * idx + 1] ^= 1
                lazy[2 * idx + 2] ^= 1
                lazy[idx] = 0

            if ss > se or us > se or ue < ss:
                return 0

            if ss >= us and se <= ue:
                return tree[idx]
            mid = (ss + se) // 2
            return query(2 * idx + 1, ss, mid, us, ue) + query(2 * idx + 2, mid + 1, se, us, ue)


        init_tree(0, 0, N - 1)
        s = sum(nums2)
        res = []
        for t, a, b in queries:
            if t == 1:
                update(0, 0, N - 1, a, b)
            elif t == 2:
                s += a * tree[0]
            else:
                res.append(s)
        return res


sol = Solution2()
tests = [
    ([1,0,1], [0,0,0], [[1,1,1],[2,1,0],[3,0,0]], [3]),
    ([1], [5], [[2,0,0],[3,0,0]], [5]),
]

for i, (nums1, nums2, queries, ans) in enumerate(tests):
    res = sol.handleQuery(nums1, nums2, queries)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
