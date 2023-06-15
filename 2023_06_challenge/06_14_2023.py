# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """LeetCode 530

        It was a shame that I forgot how BST worked.

        O(N), 80 ms, faster than 12.93%
        """
        self.res = math.inf

        def inorder(node) -> Tuple[int, int]:
            if not node:
                return math.inf, -math.inf
            l_min, l_max = inorder(node.left)
            r_min, r_max = inorder(node.right)
            self.res = min(
                self.res,
                abs(node.val - l_max),
                abs(r_min - node.val),
            )
            return min(l_min, node.val), max(r_max, node.val)

        inorder(root)
        return self.res


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
