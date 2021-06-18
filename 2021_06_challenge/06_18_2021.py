# from pudb import set_trace; set_trace()
from typing import List


class TreeNode:
    def __init__(self, r_left: int, r_right: int, r_sum: int = 0):
        """LeetCode 307

        The range is [r_left, r_right)
        """
        self.r_left = r_left
        self.r_right = r_right
        self.r_sum = r_sum
        self.left = None
        self.right = None


class NumArray1:

    def __init__(self, nums: List[int]):
        """Nothing fancy. Just a practice of building a segment tree from
        scratch.

        Initialization O(N)
        update and sumRange are both O(log(N))

        2988 ms, 42% ranking.
        """
        self.seg_tree = self.make_seg_tree(0, len(nums), nums)

    def update(self, index: int, val: int) -> None:
        self.update_seg_tree(self.seg_tree, index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.sum_seg_tree(self.seg_tree, left, right + 1)

    def make_seg_tree(self, r_left: int, r_right: int, nums: List[int]) -> TreeNode:
        if r_left + 1 == r_right:
            return TreeNode(r_left, r_right, r_sum=nums[r_left])
        root = TreeNode(r_left, r_right)
        root.left = self.make_seg_tree(r_left, (r_left + r_right) // 2, nums)
        root.right = self.make_seg_tree((r_left + r_right) // 2, r_right, nums)
        root.r_sum = root.left.r_sum + root.right.r_sum
        return root

    def update_seg_tree(self, root: TreeNode, index: int, val: int) -> int:
        if root.r_left + 1 == root.r_right:
            delta = val - root.r_sum
            root.r_sum = val
            return delta
        if root.r_left <= index < (root.r_left + root.r_right) // 2:
            delta = self.update_seg_tree(root.left, index, val)
        else:
            delta = self.update_seg_tree(root.right, index, val)
        root.r_sum += delta
        return delta

    def sum_seg_tree(self, root: TreeNode, left: int, right: int) -> int:
        if root.r_left == left and root.r_right == right:
            return root.r_sum
        mid = (root.r_left + root.r_right) // 2
        if left >= mid:
            return self.sum_seg_tree(root.right, left, right)
        elif right <= mid:
            return self.sum_seg_tree(root.left, left, right)
        else:
            return self.sum_seg_tree(root.left, left, mid) + self.sum_seg_tree(root.right, mid, right)


class NumArray2:

    def __init__(self, nums: List[int]):
        """This is a very efficient way to set up segment tree. The intuition is
        that a segment tree is always a complete binary tree. Therefore, we can
        use an array as representation. The following is almost exactly the
        copy of the official solution.

        https://leetcode.com/problems/range-sum-query-mutable/solution/
        """
        self.N = len(nums)
        self.seg_tree = self.make_seg_tree(nums)

    def update(self, index: int, val: int) -> None:
        """Update is also straightforward. We first locate the leaf by index +        N. Update that. Then we find its parent. To do so, we need to first
        check whether the leaf is a left or right leaf. If it's a left leaf,
        then its sibling is index + N + 1, otherwise index + N - 1. After locating
        the sibling, we can go to the parent and update the parent by summing
        the values of the two leaves.
        """
        pos = index + self.N
        self.seg_tree[pos] = val
        while pos > 1:
            left = right = pos
            if pos % 2:
                left -= 1
            else:
                right += 1
            pos //= 2
            self.seg_tree[pos] = self.seg_tree[left] + self.seg_tree[right]

    def sumRange(self, left: int, right: int) -> int:
        """This is a bit tricky. We first locate the left and right leaves of
        the given bounds. If the left bound is also on the left branch, then
        everything is within range and the sum can be represented by the parent
        directly. If the left bound is on the right branch, then the only thing
        that can be included is the left bound itself, and must move the left
        bound rightward by doing left + 1, such that we are completely within
        bounds again.

        The same thing happens to the right bound. If the right bound is on left
        branch, we need to include the right bound itself and move the right
        bound leftward.

        After handling the bounds, we go up to the parent for both left and right
        bounds. We terminate when left bound is larger than right bound.
        """
        lpos, rpos = self.N + left, self.N + right
        res = 0
        while lpos <= rpos:
            if lpos % 2:
                res += self.seg_tree[lpos]
                lpos += 1
            if not rpos % 2:
                res += self.seg_tree[rpos]
                rpos -= 1
            lpos //= 2
            rpos //= 2
        return res

    def make_seg_tree(self, nums: List[int]) -> List[int]:
        """This one is easy to understand. We go bottom up. We first fill out
        the leaves. Given N leaves in a complete binary tree, there are 2 * N - 1
        total nodes. However, since we are using 1-based addressing, we have to
        create 2N length array to hold the tree. Recall that in a 1-based setting
        a node at index i has left child at 2 * i and right child 2 * i + 1.
        """
        seg_tree = [0] * (2 * len(nums))
        for i, n in enumerate(nums):
            seg_tree[i + self.N] = n
        for j in range(self.N - 1, 0, -1):
            seg_tree[j] = seg_tree[2 * j] + seg_tree[2 * j + 1]
        return seg_tree


class NumArray3:

    def __init__(self, nums: List[int]):
        """Binary Indexed Tree

        https://en.wikipedia.org/wiki/Fenwick_tree

        BIT is a 1-based array.

        Let j be the index in BIT, if j == 2^a (a != 0),
        then BIT[j] = nums[0] + nums[1] + ... + nums[j]

        If j == 2^a + 2^b + ... + 2^k (0 < a < b < ... < k),
        then BIT[j] = nums[2^k + 1] + nums[2^k + 2] + ... + nums[j]

        if j == 1 + 2^a + 2^b + ... + 2^k (0 < a < b < ... < k),
        then BIT[j] = nums[j]

        i & (-i) returns the least significant bit. e.g. 6 & (-6) = 2
        """
        self.N = len(nums) + 1
        self.nums = nums
        self.BIT = [0] * self.N
        for i, n in enumerate(nums):
            self._update(i + 1, n)

    def _update(self, i: int, delta: int) -> None:
        while i < self.N:
            self.BIT[i] += delta
            i += (i & (-i))

    def _query(self, i: int) -> int:
        res = 0
        while i > 0:
            res += self.BIT[i]
            i -= (i & (-i))
        return res

    def update(self, index: int, val: int) -> None:
        self._update(index + 1, val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self._query(right + 1) - self._query(left)


# sol = Solution3()
# tests = [
#     ('abab', True),
#     ('aba', False),
#     ('abcabcabcabc', True),
#     ('abcabcababcabcab', True),
#     ('abcbac', False),
#     ('aabaabaab', True),
#     ('a', False),
#     ('aaaaaaa', True),
#     ('aaaaab', False),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.repeatedSubstringPattern(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
