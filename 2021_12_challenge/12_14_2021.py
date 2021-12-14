# from pudb import set_trace; set_trace()
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """LeetCode 938

        DFS, O(N), 272 ms, 29% ranking.
        """
        if not root:
            return 0
        return self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high) + (root.val if low <= root.val <= high else 0)
        

class Solution2:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """Oops, didn't realize that this is a BST. With BST, we can make
        changes to the range, and we can avoid visiting an entire branch if it
        is outside range.
        
        O(N), 220 ms, 54% ranking.
        """
        if not root:
            return 0
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        return self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high) + root.val


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
