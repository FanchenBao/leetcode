# from pudb import set_trace; set_trace()
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """LeetCode 129

        BFS. At each node, accumulate the number so far. Aggregate the resutl
        when a leaf node is encountered.

        O(N), 24 ms, 96% ranking
        """
        queue = [(root, root.val)]
        res = 0
        while queue:
            temp = []
            for node, val in queue:
                if not node.left and not node.right:
                    res += val
                else:
                    if node.left:
                        temp.append((node.left, val * 10 + node.left.val))
                    if node.right:
                        temp.append((node.right, val * 10 + node.right.val))
            queue = temp
        return res


class Solution:
    def sumNumbers(self, root: Optional[TreeNode], val: int = 0) -> int:
        """
        DFS, similar idea as above.

        O(N)
        """
        if not root:
            return 0
        cur = 10 * val + root.val
        if not root.left and not root.right:
            return cur
        else:
            return self.sumNumbers(root.left, val=cur) + self.sumNumbers(root.right, val=cur)

        


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
