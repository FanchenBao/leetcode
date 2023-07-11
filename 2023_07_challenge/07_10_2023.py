# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """LeetCode 111

        O(N), 493 ms, faster than 88.88%
        """
        if not root:
            return 0
        queue = [root]
        lvl = 0
        while queue:
            tmp = []
            for node in queue:
                if not node.left and not node.right:
                    return lvl + 1
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue = tmp
            lvl += 1


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
