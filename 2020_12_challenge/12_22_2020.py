# from pudb import set_trace; set_trace()
from typing import List, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """Una problema facil. DFS para obtener la altura del arbo, y si los
        hijos son equilibrado. Regresa la nueva alta y el equilibrio del
        arbo actual.

        O(N), 52 ms, 62% ranking.
        """

        def helper(node: TreeNode) -> Tuple[bool, int]:
            if not node:
                return True, 0
            l_balanced, l_height = helper(node.left)
            r_balanced, r_height = helper(node.right)
            if l_balanced and r_balanced and abs(l_height - r_height) <= 1:
                return True, max(l_height, r_height) + 1
            return False, -1

        return helper(root)[0]


# sol = Solution3()
# tests = [
#     # ([1, 2, 3, 1], 3, 0, True),
#     # ([1, 0, 1, 1], 1, 2, True),
#     ([1, 5, 9, 1, 5, 9], 2, 3, False),
#     # ([1, 4, 9, 1, 4, 9], 1, 3, True),
#     # ([-1, -1], 1, -1, False),
#     # ([1, 3, 6, 2], 1, 2, True),
# ]

# for i, (nums, k, t, ans) in enumerate(tests):
#     res = sol.containsNearbyAlmostDuplicate(nums, k, t)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
