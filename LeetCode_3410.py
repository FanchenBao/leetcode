# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class SegTree:
    def __init__(self, N: int) -> None:
        # each node contains four values as follows:
        # [max_subarray_sum, total_sum, max_prefix_sum, max_suffix_sum]
        self.N = N
        self.MAX = 10**12
        tree_size = 2 ** (math.ceil(math.log2(self.N)) + 1)
        self.tree = [[-self.MAX, 0, -self.MAX, -self.MAX] for _ in range(tree_size)]

    def _update(self, idx: int, val: int, rl: int, rr: int, node: int) -> None:
        if rl == rr:
            for i in range(4):
                self.tree[node][i] = val
            if val == -self.MAX:  # indicates removal of val at idx
                self.tree[node][1] = 0
            return
        mid = (rl + rr) // 2
        ln, rn = 2 * node + 1, 2 * node + 2
        if idx <= mid:
            self._update(idx, val, rl, mid, ln)
        else:
            self._update(idx, val, mid + 1, rr, rn)
        self.tree[node][0] = max(
            self.tree[ln][0],
            self.tree[rn][0],
            self.tree[ln][3] + self.tree[rn][2],
        )
        self.tree[node][1] = self.tree[ln][1] + self.tree[rn][1]  # total sum
        self.tree[node][2] = max(
            self.tree[ln][2], self.tree[ln][1] + self.tree[rn][2]
        )  # max prefix sum
        self.tree[node][3] = max(
            self.tree[rn][3], self.tree[ln][3] + self.tree[rn][1]
        )  # max suffix sum

    def update(self, idx: int, val: int) -> None:
        self._update(idx, val, 0, self.N - 1, 0)


class Solution:
    def maxSubarraySum(self, nums: List[int]) -> int:
        """
        We will use segment tree.

        Each node in the segment tree records the max subarray sum, total sum,
        max prefix sum, and max suffix sum. We can always use these values of
        the two children to update them in the parent.

        Also, the segment tree only needs to implement the update function,
        because the value we want has already been computed inside each node.

        O(NlogN)
        """
        MAX = 10**12
        seg = SegTree(len(nums))
        num_to_idx = defaultdict(list)
        for i, n in enumerate(nums):
            seg.update(i, n)
            num_to_idx[n].append(i)

        res = seg.tree[0][0]
        if seg.tree[0][0] == seg.tree[0][1]:
            # all elements in nums are non-negative
            return res
        # backtracking by removing each unique number, find the max subarray
        # sum, keep track of it, and add the number back
        for n, indices in num_to_idx.items():
            if n < 0:
                # remove value n at each index
                for i in indices:
                    seg.update(i, -MAX)
                res = max(res, seg.tree[0][0])
                # backtracking
                for i in indices:
                    seg.update(i, n)
        return res


sol = Solution()
tests = [([-3, 2, -2, -1, 3, -2, 3], 7)]

for i, (nums, ans) in enumerate(tests):
    res = sol.maxSubarraySum(nums)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
