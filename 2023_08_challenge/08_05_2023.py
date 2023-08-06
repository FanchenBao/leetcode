# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        """LeetCode 95

        Since n is small, we can use DP and bit mask to record the state of
        which values have been taken and which have not.

        The difficulty is to figure out the available states for the left and
        right subtrees.

        51 ms, faster than 98.32%
        """

        @lru_cache(maxsize=None)
        def create(state: int) -> List[Optional[TreeNode]]:
            res = []
            for i in range(n):
                if (1 << i) & state:
                    new_state = state ^ (1 << i)
                    for left in create(new_state & ((1 << i) - 1)):
                        for right in create(new_state & (((1 << n) - 1) ^ ((1 << i) - 1))):
                            res.append(TreeNode(val=i + 1, left=left, right=right))
            return res if res else [None]

        return create((1 << n) - 1)


class Solution2:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        """Much much cleaner solution.

        49 ms, faster than 98.84%
        """

        @lru_cache(maxsize=None)
        def create(lo: int, hi: int) -> List[Optional[TreeNode]]:
            """Produce all BST in the range lo to hi"""
            if lo > hi:
                return [None]
            return [
                TreeNode(val=v, left=left, right=right)
                for v in range(lo, hi + 1)
                for left in create(lo, v - 1)
                for right in create(v + 1, hi)
            ]

        return create(1, n)
        

# sol = Solution2()
# tests = [
#     ("hello", "holle"),
#     ("leetcode", "leotcede"),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
