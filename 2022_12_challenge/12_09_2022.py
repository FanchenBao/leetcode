# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """LeetCode 1026

        Find the min max of each subtree, and compute their difference with
        current node.val. Keep track of the max difference.

        O(N), 37 ms, faster than 97.32%
        """
        self.res = 0

        def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
            cur_max, cur_min = node.val, node.val
            if node.left:
                max_l, min_l = dfs(node.left)
                self.res = max([self.res, abs(node.val - max_l), abs(node.val - min_l)])
                cur_max = max(max_l, cur_max)
                cur_min = min(min_l, cur_min)
            if node.right:
                max_r, min_r = dfs(node.right)
                self.res = max([self.res, abs(node.val - max_r), abs(node.val - min_r)])
                cur_max = max(max_r, cur_max)
                cur_min = min(min_r, cur_min)
            return cur_max, cur_min

        dfs(root)
        return self.res


class Solution2:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """For the lols
        """
        self.res = 0

        def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
            if not node:
                return -1, -1
            max_l, min_l = dfs(node.left)
            max_r, min_r = dfs(node.right)
            self.res = max([
                self.res,
                abs(node.val - max_l) * int(max_l >= 0),
                abs(node.val - max_r) * int(max_r >= 0),
                abs(node.val - min_l) * int(min_l >= 0),
                abs(node.val - min_r) * int(min_r >= 0),
            ])
            return (
                max([node.val, max_l * int(max_l >= 0), max_r * int(max_r >= 0)]),
                min([node.val, min_l if min_l >= 0 else math.inf, min_r if min_r >= 0 else math.inf]),
            )

        dfs(root)
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
