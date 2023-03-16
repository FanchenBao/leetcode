# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        """LeetCode 958

        Pretty dumb BFS.

        O(N), 40 ms, faster than 41.11%
        """
        queue = [root]
        lvl = 0
        while queue:
            tmp = []
            first_none = math.inf  # first index in tmp that a None would've been added
            i = 0
            for node in queue:
                if node.left:
                    tmp.append(node.left)
                    i += 1
                else:
                    first_none = min(first_none, i)
                if node.right:
                    tmp.append(node.right)
                    i += 1
                else:
                    first_none = min(first_none, i)
            if len(queue) != 2**lvl and tmp:  # any level before the last is not power of 2
                return False
            if first_none < len(tmp):  # any level where the None not happening at the end
                return False
            lvl += 1
            queue = tmp
        return True


class Solution2:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        """I was so dumb. All we need to check is whether during BFS, a None
        node is encountered.

        O(N), 38 ms, faster than 56.30%
        """
        queue = [root]
        has_none = False
        while queue:
            tmp = []
            for node in queue:
                if not node:
                    has_none = True
                else:
                    if has_none:
                        return False
                    tmp.append(node.left)
                    tmp.append(node.right)
            queue = tmp
        return True


# sol = Solution2()
# tests = [
#     ("hello", "holle"),
#     ("leetcode", "leotcede"),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
