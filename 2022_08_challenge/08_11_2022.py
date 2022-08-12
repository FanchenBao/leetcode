# from pudb import set_trace; set_trace()
from typing import List
import math


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def isValidBST(self, root: Optional[TreeNode], par=math.inf, is_left=True) -> bool:
#         if not root:
#             return True
#         is_left_bst = self.isValidBST(root.left, par=root.val, is_left=True)
#         is_right_bst = self.isValidBST(root.right, par=root.val, is_left=False)
#         if is_left:
#             is_left_good = (root.val > root.left.val) if root.left else True
#             is_right_good = (root.val < root.right.val and root.right.val < par) if root.right else True
#         else:
#             is_left_good = (root.val > root.left.val and root.left.val > par) if root.left else True
#             is_right_good = (root.val < root.right.val) if root.right else True
#         return all([is_left_good, is_right_good, is_left_bst, is_right_bst])


class Solution1:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """LeetCode 98

        Traverse pre-order?? and then check whether the resulting array is
        strictly increasing.

        O(N), 80 ms, faster than 32.73%
        """
        array = []

        def traverse(node: Optional[TreeNode]) -> bool:
            if node:
                traverse(node.left)
                array.append(node.val)
                traverse(node.right)
        
        traverse(root)
        for i in range(1, len(array)):
            if array[i] <= array[i - 1]:
                return False
        return True


class Solution2:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """Recursion

        O(N), 64 ms, faster than 62.86%
        """
        def check_bst(node: Optional[TreeNode]) -> Tuple[int, int, bool]:
            if not node:
                return math.inf, -math.inf, True
            lmin, lmax, l_bst = check_bst(node.left)
            rmin, rmax, r_bst = check_bst(node.right)
            c_bst = l_bst and r_bst and lmax < node.val and rmin > node.val
            return min(lmin, rmin, node.val), max(lmax, rmax, node.val), c_bst

        return check_bst(root)[2]


# sol = Solution()
# tests = [
#     ([4,2,1,3], [[1,2],[2,3],[3,4]]),
#     ([1,3,6,10,15], [[1,3]]),
#     ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
# ]

# for i, (arr, ans) in enumerate(tests):
#     res = sol.minimumAbsDifference(arr)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
