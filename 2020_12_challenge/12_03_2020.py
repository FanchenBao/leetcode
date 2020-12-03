# from pudb import set_trace; set_trace()
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        """Naive method, use O(N) extra space. 32 ms, 59% ranking."""
        sorted_vals = []

        def in_order(node: TreeNode):
            if node:
                in_order(node.left)
                sorted_vals.append(node.val)
                in_order(node.right)

        in_order(root)
        dummy = TreeNode()
        node = dummy
        for val in sorted_vals:
            node.right = TreeNode(val=val)
            node = node.right
        return dummy.right


class Solution2:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        """Directly building the result tree, 36 ms, 11% ranking."""
        def in_order(node: TreeNode, end_node: TreeNode):
            """This function returns the last node in the new tree when the
            subtree rooted at node is converted.
            """
            end_node = in_order(node.left, end_node) if node.left else end_node
            end_node.right = TreeNode(val=node.val)
            return in_order(node.right, end_node.right) if node.right else end_node.right

        dummy = TreeNode()
        in_order(root, dummy)
        return dummy.right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        """Modify tree in place 24 ms, 94% ranking"""
        def in_order(node: TreeNode):
            """Acquire the front and end node of the substree rooted at node
            after transformation.
            """
            if not node:
                return None, None
            front, left_mid = in_order(node.left)
            mid = TreeNode(val=node.val)
            if not front:
                front = mid
            if left_mid:
                left_mid.right = mid
            right_mid, end = in_order(node.right)
            if right_mid:
                mid.right = right_mid
            if not end:
                end = mid
            return front, end

        return in_order(root)[0]
        


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
