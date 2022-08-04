# from pudb import set_trace; set_trace()
from typing import List
from bisect import bisect_right


class MyCalendar:

    def __init__(self):
        """LeetCode 729

        O(NlogN) per book call. Not the most efficient for sure.
        1429 ms, faster than 14.59%
        """
        self.cal = {}

    def book(self, start: int, end: int) -> bool:
        if not self.cal:
            self.cal[start] = end
            return True
        starts = sorted(self.cal)
        idx = bisect_right(starts, start)
        if idx > 0 and self.cal[starts[idx - 1]] > start:
            return False
        if idx < len(starts) and starts[idx] < end:
            return False
        self.cal[start] = end
        return True


class TreeNode:
    def __init__(self, lo: int, hi: int) -> None:
        self.lo = lo
        self.hi = hi
        self.left = None
        self.right = None


class MyCalendar:

    def __init__(self):
        """Binary search tree solution. Best case O(NlogN), worst O(N^2)

        382 ms, faster than 64.28%

        It's a much better runtime than sorting and binary search, which means
        the input is pretty balanced already.
        """
        self.root = None

    def _insert(self, node: TreeNode, lo: int, hi: int) -> bool:
        if lo >= node.hi:
            if node.right is None:
                node.right = TreeNode(lo, hi)
                return True
            return self._insert(node.right, lo, hi)
        if hi <= node.lo:
            if node.left is None:
                node.left = TreeNode(lo, hi)
                return True
            return self._insert(node.left, lo, hi)
        return False

    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            self.root = TreeNode(start, end)
            return True
        return self._insert(self.root, start, end)


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
