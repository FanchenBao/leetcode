# from pudb import set_trace; set_trace()
from typing import List, Optional
import math
from functools import lru_cache


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @lru_cache(maxsize=None)
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        """LeetCode 894

        I was way overthinking this. Just go through each subtree's count from
        1 to n, all odd values, and that's it.

        O(2^(N/2)), 173 ms.
        """
        if n == 1:
            return [TreeNode()]
        if n % 2 == 0:
            return None
        res = []
        n -= 1
        for i in range(1, n, 2):
            for r1 in self.allPossibleFBT(i):
                for r2 in self.allPossibleFBT(n - i):
                    res.append(TreeNode(left=r1, right=r2))
        return res


# sol = Solution()
# tests = [
#     (7, None),
#     # ("leetcode", "leotcede"),
# ]

# for i, (n, ans) in enumerate(tests):
#     res = sol.allPossibleFBT(n)
#     print(res)
#     # if res == ans:
#     #     print(f'Test {i}: PASS')
#     # else:
#     #     print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')