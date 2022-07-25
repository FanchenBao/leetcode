# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_left
from collections import deque


class TreeNode:
    def __init__(self, rl: int, rr: int) -> None:
        self.rl = rl
        self.rr = rr
        self.left = None
        self.right = None
        self.count = 0


class SegTree:
    def __init__(self, rmin: int, rmax: int):
        self.root = TreeNode(rmin, rmax)

    def update(self, val: int) -> None:
        self._update(self.root, val)

    def query(self, rl: int, rr: int) -> int:
        return self._query(self.root, rl, rr)

    def _update(self, node: TreeNode, val: int) -> None:
        if node.rl == node.rr == val:
            node.count += 1
            return
        mid = (node.rl + node.rr) // 2
        if val <= mid:
            if not node.left:
                node.left = TreeNode(node.rl, mid)
            self._update(node.left, val)
        else:
            if not node.right:
                node.right = TreeNode(mid + 1, node.rr)
            self._update(node.right, val)
        node.count = (node.left.count if node.left else 0) + (node.right.count if node.right else 0)

    def _query(self, node: TreeNode, rl: int, rr: int) -> int:
        if not node:
            return 0
        if node.rl == rl and node.rr == rr:
            return node.count
        mid = (node.rl + node.rr) // 2
        if rr <= mid:
            return self._query(node.left, rl, rr)
        if rl > mid:
            return self._query(node.right, rl, rr)
        return self._query(node.left, rl, mid) + self._query(node.right, mid + 1, rr)


class SegTree2:
    def __init__(self, rmin: int, rmax: int):
        self.tree = [0] * (2 ** (math.ceil(math.log2(rmax - rmin + 1)) + 1))
        self.rmin = rmin
        self.rmax = rmax

    def update(self, val: int) -> None:
        self._update(0, val, self.rmin, self.rmax)

    def query(self, rl: int, rr: int) -> int:
        return self._query(0, rl, rr, self.rmin, self.rmax)

    def _update(self, idx: int, val: int, rl: int, rr: int) -> None:
        if rl == rr:
            self.tree[idx] += 1
            return
        mid = (rl + rr) // 2
        li, ri = 2 * idx + 1, 2 * idx + 2
        if val <= mid:
            self._update(li, val, rl, mid)
        else:
            self._update(ri, val, mid + 1, rr)
        self.tree[idx] = self.tree[li] + self.tree[ri]

    def _query(self, idx: int, rl: int, rr: int, _rl: int, _rr: int) -> int:
        if rl > rr:
            return 0
        if _rl == _rr or (_rl == rl and _rr == rr):
            return self.tree[idx]
        mid = (_rl + _rr) // 2
        li, ri = 2 * idx + 1, 2 * idx + 2
        if rr <= mid:
            return self._query(li, rl, rr, _rl, mid)
        if rl > mid:
            return self._query(ri, rl, rr, mid + 1, _rr)
        return self._query(li, rl, mid, _rl, mid) + self._query(ri, mid + 1, rr, mid + 1, _rr)


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

        The meaning of "values" is defined by the `delta` parameter
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


class Solution1:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """LeetCode 315

        I tried segment tree with tree node implementation, TLE; with array
        implementation, TLE; with the same implementation as my attempt last
        year, TLE.

        The only thing that worked is BIT. Maybe it's time to revisit BIT and
        try to understand it.

        But I am disappointed and mad that I failed to realize the problem is
        a straightforward segment tree.

        O(NlogN), 3329 ms, faster than 73.43%
        """
        min_n, max_n = min(nums), max(nums)
        bit = BIT(max_n - min_n + 1)
        res = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            bit.update(nums[i] - min_n + 1, 1)
            res[i] = bit.query(nums[i] - min_n)
        return res


class Solution2:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """This is a really really smart solution.

        https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/445769/merge-sort-CLEAR-simple-EXPLANATION-with-EXAMPLES-O(n-lg-n)

        Use merge sort. Since at each level, we always merge the left half and
        the right half, so naturally all the smaller values on the right half
        can count towards the result of the values on the left half that are
        bigger. And merge sort already does the comparison for us. All we need
        to do is to keep track of the count of the values on the right that are
        smaller.

        O(NlogN), 3002 ms, faster than 81.89%
        """
        N = len(nums)
        res = [0] * N
        nums = [(n, i) for i, n in enumerate(nums)]

        def merge_sort(lo: int, hi: int) -> List[int]:
            if lo == hi:
                return [nums[lo]]
            mid = (lo + hi) // 2
            sl, sr = merge_sort(lo, mid), merge_sort(mid + 1, hi)
            c = 0
            i = j = 0
            r = []
            while i < len(sl) and j < len(sr):
                if sl[i][0] <= sr[j][0]:
                    r.append(sl[i])
                    res[sl[i][1]] += c
                    i += 1
                else:
                    r.append(sr[j])
                    j += 1
                    c += 1
            while i < len(sl):
                r.append(sl[i])
                res[sl[i][1]] += c
                i += 1
            while j < len(sr):
                r.append(sr[j])
                j += 1
            return r

        merge_sort(0, N - 1)
        return res


sol = Solution2()
tests = [
    ([5,2,6,1], [2, 1, 1, 0]),
    ([-1], [0]),
    ([-1, -1], [0, 0]),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.countSmaller(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
