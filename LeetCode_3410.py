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

        O(NlogN) 14780 ms, 5%
        """
        MAX = 10**12
        seg = SegTree(len(nums))
        num_to_idx = defaultdict(list)
        has_neg = False
        for i, n in enumerate(nums):
            has_neg |= n < 0
            seg.update(i, n)
            num_to_idx[n].append(i)

        if not has_neg:  # all elements are non-negative
            return seg.tree[0][0]

        res = seg.tree[0][0]
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


class Solution2:
    def maxSubarraySum(self, nums: List[int]) -> int:
        """
        This solution is inspired by
        https://leetcode.com/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/solutions/6231124/c-segment-tree-is-hard-use-dp-with-kadane-time-complexity-o-n

        If we want to find the max subarray sum after removing all occurrences
        of x, this means at some index j, we have

        subsum = presum[j] - (presum[i - 1] + sum(x for x in i...j))

        where presum[i - 1] + sum(x for x in i...j) is smallest.

        We can use pre[x] to represent the smallest expression above. As we
        iterate through nums, we update all pre[x]. Thus, for each nums[j],
        we will be able to find the max subarray sum possible ending at nums[j]
        with some x deleted.

        We only delete nums[j] if it is negative. When we delete nums[j], there
        are two scenarios to consider. First, if there is no additional
        nums[j] between the end of pre[0] and j, then the smallest pre with
        only one nums[j] deleted should be pre[0] + n.

        However, if there have been other nums[j] before, then we have
        pre[nums[j]]. Then the smallest pre can be pre[nums[j]] + nums[j]

        We do not know which of the two scenarios is true, so we take the
        smaller between the two.

        And we designate pre[0] as the min prefix sum without deleting anything.
        At each nums[j], we can of course also choose not to delete it.

        O(N), 247 ms, 86%
        """
        psum = 0
        pre = {}
        pre[0] = 0  # without deleting anything, the starting point is 0
        lowest = 0  # smallest pre
        res = -10000000
        for n in nums:
            psum += n
            res = max(res, psum - lowest)
            if n < 0:
                # option 1: delete n
                if n not in pre:  # scenario 1: first n encountered
                    pre[n] = pre[0] + n
                else:  # scneario 2: n has been encountered before
                    # We can either build on top of the previous result of
                    # pre[n], or we check if it is possible to use pre[0],
                    # provided that there is no other n between the end of
                    # pre[0] and the current n.
                    pre[n] = min(pre[0], pre[n]) + n
                lowest = min(lowest, pre[n])
            # option 2: do not delete n
            pre[0] = min(pre[0], psum)
            lowest = min(lowest, pre[0])
        return res


sol = Solution()
tests = [([12, 23, -1, -30, 31, 5], 70)]

for i, (nums, ans) in enumerate(tests):
    res = sol.maxSubarraySum(nums)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
