# from pudb import set_trace; set_trace()
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def helper(self, node: TreeNode, min_anc: int, max_anc: int, res: List[int]) -> Tuple[int, int]:
        if not node:
            return -1, -1
        res[0] = max([res[0], abs(node.val - min_anc), abs(node.val - max_anc)])
        min_cur, max_cur = min(min_anc, node.val), max(max_anc, node.val)
        min_l, max_l = self.helper(node.left, min_cur, max_cur, res)
        if min_l < 0:
            min_l = max_l = node.val
        min_r, max_r = self.helper(node.right, min_cur, max_cur, res)
        if min_r < 0:
            min_r = max_r = node.val
        res[0] = max([
            res[0],
            abs(node.val - min_l),
            abs(node.val - max_l),
            abs(node.val - min_r),
            abs(node.val - max_r),
        ])
        return min([node.val, min_l, min_r]), max([node.val, max_l, max_r])

    def maxAncestorDiff(self, root: TreeNode) -> int:
        """19% ranking
        
        For each node, find its max and min ancestor. Recursively find its max
        and min children. Compute and store the max diff. Runtime is O(N).
        """
        res = [0]
        self.helper(root, root.val, root.val, res)
        return res[0]


class Solution2:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        """60% ranking
        
        We only need to consider the ancestor. No need to consider the children
        because the children will be taken care of when the children become
        the root.
        """
        self.res = 0
        
        def helper(node: TreeNode, max_anc: int, min_anc: int):
            if not node:
                return
            self.res = max([self.res, abs(node.val - max_anc), abs(node.val - min_anc)])
            max_anc, min_anc = max(node.val, max_anc), min(node.val, min_anc)
            helper(node.left, max_anc, min_anc)
            helper(node.right, max_anc, min_anc)

        helper(root, root.val, root.val)
        return self.res
        


class Solution3:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        """99% ranking
        
        Consider each root-to-leaf path. Each path contains only one max, min
        pair. We can traverse the tree, and once reaching a leaf, we report
        the difference between the min and max encountered on the path. We
        find the max of min, max difference in all root-to-leaf paths.

        This method is even faster becasue the number of min() and max() calls
        is half of soultion2.
        """
        def helper(node: TreeNode, max_: int, min_: int):
            if not node:
                return max_ - min_
            max_, min_ = max(node.val, max_), min(node.val, min_)
            return max(
                helper(node.left, max_, min_), 
                helper(node.right, max_, min_),
            )

        return helper(root, root.val, root.val)


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
