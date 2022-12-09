# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """LeetCode 872

        57 ms, faster than 62.56%
        """

        def get_leaves(node: Optional[TreeNode], leaves: List) -> None:
            if node:
                get_leaves(node.left, leaves)
                if not node.left and not node.right:
                    leaves.append(node.val)
                get_leaves(node.right, leaves)

        l1, l2 = [], []
        get_leaves(root1, l1)
        get_leaves(root2, l2)
        return l1 == l2
        

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
