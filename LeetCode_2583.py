# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        """BFS

        O(NlogN), 567 ms, faster than 92.69% 
        """
        queue = [root]
        sums = []
        while queue:
            tmp = []
            sums.append(0)
            for node in queue:
                sums[-1] += node.val
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue = tmp
        sums.sort()
        return sums[-k] if k <= len(sums) else -1

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
