# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """LeetCode 222

        Naive solution. Didn't take advantage of the tree being complete.

        O(N), 209 ms, faster than 22.26%
        """
        if not root:
            return 0
        res = 0
        queue = [root]
        while queue:
            res += len(queue)
            tmp = []
            for node in queue:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue = tmp
        return res


class Solution2:
    def get_height(self, node: Optional[TreeNode]) -> int:
        res = 0
        while node:
            res += 1
            node = node.left
        return res

    def countNodes(self, root: Optional[TreeNode]) -> int:
        """This method takes full advantage of the tree being complete. We use
        binary search to eliminate a complete complete tree at each step. If
        the max height of the two subtrees are the same, that means the left
        subtree must be complete complete. Otherwise, the right subtree must be
        complete complete.

        O((logN)^2), 87 ms, faster than 91.47%
        """
        if not root:
            return 0
        hl = self.get_height(root.left)
        hr = self.get_height(root.right)
        if hl == hr:  # left subtree has leaf also complete
            return 1 + 2**hl - 1 + self.countNodes(root.right)
        return 1 + 2**hr - 1 + self.countNodes(root.left)
        





# sol = Solution()
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
