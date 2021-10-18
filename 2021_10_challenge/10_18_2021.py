# from pudb import set_trace; set_trace()
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        """LeetCode 993

        Standard BFS solution. The only trick is to include the current
        node's parent when pushing it into the queue. Then whenever x or y is
        encountered, we record its parent. Finally, we compare the parent. If
        both x and y are found on the same level and their parents are different
        we return True, otherwise False. If only one of x and y is found, we
        immediately return False because that indicates that x and y are on
        different levels.

        O(N), 36 ms, 52% ranking.
        """
        queue = [[0, root]]
        while queue:
            temp = []
            xp, yp = -1, -1
            for p, node in queue:
                if node.val == x:
                    xp = p
                if node.val == y:
                    yp = p
                if node.left:
                    temp.append([node.val, node.left])
                if node.right:
                    temp.append([node.val, node.right])
            if xp >= 0 and yp >= 0:
                return xp != yp
            if xp * yp <= 0:
                return False
            queue = temp
        return False
        


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
