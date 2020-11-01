# from pudb import set_trace; set_trace()
from typing import List
import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.

        98% ranking. However, the space complexity is O(N).
        We first perform inorder traverse of the BST and store the results in
        an array. We then compare this array with its sorted version to
        identify the swapped values. We then traverse the BST again and swap
        the value back.
        """
        vals = []

        def inorder(node: TreeNode):
            if node:
                inorder(node.left)
                vals.append(node.val)
                inorder(node.right)
        
        inorder(root)  # acquire the BST values in order
        for v, sv in zip(vals, sorted(vals)):
            if v != sv:  # the swapped values
                break

        def swap_back(node: TreeNode):
            if node:
                swap_back(node.left)
                if node.val == v:
                    node.val = sv
                elif node.val == sv:
                    node.val = v
                swap_back(node.right)

        swap_back(root)



class Solution2:
    def recoverTree(self, root: TreeNode) -> None:
        """O(1) space complexity.

        The only difference is that we do not record the entire inorder array,
        but just the two pairs of mismatched values (some value might be
        repeated in the two pairs, but that's fine). Then we do the same as
        Solution1 to find the actual swapped values and swap back in the
        original tree. Since the two pairs of mismatched values only takes
        O(4) space, this is an O(1) space complexity solution.

        UPDATE: This is NOT O(1) space complexity, because recursion is never
        O(1). The real O(1) solution requires Morrison Traversal.

        See here: https://www.cnblogs.com/AnnieKim/archive/2013/06/15/morristraversal.html
        for a description of Morrison Traversal. I actually have learned about
        this in data structure class, but apparently I have forgotten this
        O(1) space O(N) time traversal method.
        """
        sn = []  # potentially swapped nodes, length equals four
        pre = [TreeNode(val=-math.inf)]

        def inorder(node: TreeNode):
            if node:
                inorder(node.left)
                if node.val < pre[0].val:
                    sn.extend([pre[0], node])
                pre[0] = node
                inorder(node.right)

        inorder(root)
        # the swapped values will always be the first and last values of the
        # sn list. Consider 1, 2, 4, 3, 5. Adjacent values 3, 4 are
        # swapped, thus sn = [4, 3]. Consider 1, 5, 3, 4, 2. We have
        # two pairs of potential swaps (5, 3) and (4, 2). The swapped are 5, 2,
        # which is the first and last elements of vals = [5, 3, 4, 2]. From
        # another perspective, any swap would place a big value to the front
        # and a small value at the back. So the first time a wrong order is
        # encountered, the big value must be the swapped. And the second time,
        # the smaller value.
        sn[0].val, sn[-1].val = sn[-1].val, sn[0].val
        




        


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
