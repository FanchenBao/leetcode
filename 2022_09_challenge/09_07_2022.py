# from pudb import set_trace; set_trace()
from typing import List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        """LeetCode 606

        This problem is kind of stupid. The "one-to-one" mapping between the
        string and binary tree doesn't make much sense. Eventually, we figure
        out that the empty paren must be present when a parent's left node is
        empty but right node is not. If it is the other way around or a parent
        has no children, then we do not use empty paren.

        Useful test cases:
        [1,2,3,null,4]
        [1,2,3,4]
        [1,null,2,null,3]
        [1,2,3,null,4,null,5]
        [3,2,4,null,null,1]
        [1,2,3,4,null,null,5]

        O(N), 72 ms, faster than 67.73%
        """
        if not root.left and not root.right:
            return str(root.val)
        if root.left and not root.right:
            return f'{root.val}({self.tree2str(root.left)})'
        if root.right and not root.left:
            return f'{root.val}()({self.tree2str(root.right)})'
        return f'{root.val}({self.tree2str(root.left)})({self.tree2str(root.right)})'


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
