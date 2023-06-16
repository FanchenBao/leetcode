# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """We did this in-place. But it is not that much work to create a new
        tree.

        O(N), 1356 ms, faster than 80.42% 
        """
        queue = [(-1, root)]
        pre_total = root.val
        pre_sib_sums = {-1: root.val}
        while queue:
            tmp = []
            cur_total = 0
            cur_sib_sums = defaultdict(int)
            for par_id, node in queue:
                if node.left:
                    tmp.append((id(node), node.left))
                    cur_total += node.left.val
                    cur_sib_sums[id(node)] += node.left.val
                if node.right:
                    tmp.append((id(node), node.right))
                    cur_total += node.right.val
                    cur_sib_sums[id(node)] += node.right.val
                node.val = pre_total - pre_sib_sums[par_id]
            pre_total = cur_total
            pre_sib_sums = cur_sib_sums
            queue = tmp
        return root


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
