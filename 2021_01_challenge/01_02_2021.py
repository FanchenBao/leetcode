# from pudb import set_trace; set_trace()
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        """Since the values are unique for each node, this question is an easy
        one. Simply DFS and look for the node that has the same value as the
        target and we are done.

        The extra question is much harder, as it allows repeats in the value.

        O(N), 608 ms, 88% ranking.
        """

        def dfs(node: TreeNode) -> TreeNode:
            if node:
                if node.val == target.val:
                    return node
                return dfs(node.left) or dfs(node.right)

        return dfs(cloned)


class Solution2:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        """Not using the value but the reference itself.

        O(N), 640 ms, 37% ranking.
        """

        def dfs(o_node: TreeNode, c_node: TreeNode) -> TreeNode:
            if o_node:
                if id(o_node) == id(target):
                    return c_node
                return dfs(o_node.left, c_node.left) or dfs(o_node.right, c_node.right)

        return dfs(original, cloned)


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
