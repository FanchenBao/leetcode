# from pudb import set_trace; set_trace()
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """LeetCode 106

        Very good question. I did it more than a year ago, but this time I
        almost hit the right direction from the beginning. The idea is to use
        the postorder to locate the root, and use the inorder to split the
        building into left and right subtree. The one trick is to use a hash map
        to quickly query the index of any root value in inorder array.

        60 ms, 73% ranking.
        """
        self.pi = len(postorder) - 1
        inorder_idx = {val: i for i, val in enumerate(inorder)}

        def build(lo: int, hi: int) -> TreeNode:
            if lo > hi:
                return None
            i = inorder_idx[postorder[self.pi]]
            root = TreeNode(val=inorder[i])
            self.pi -= 1
            root.right = build(i + 1, hi)
            root.left = build(lo, i - 1)
            return root

        return build(0, len(inorder) - 1)
        

# sol = Solution3()
# tests = [
#     ('abab', True),
#     ('aba', False),
#     ('abcabcabcabc', True),
#     ('abcabcababcabcab', True),
#     ('abcbac', False),
#     ('aabaabaab', True),
#     ('a', False),
#     ('aaaaaaa', True),
#     ('aaaaab', False),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.repeatedSubstringPattern(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
