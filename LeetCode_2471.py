# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_left


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        """I thought this would time out, because at each level, we do a sort
        and we do hopping. But it worked.

        The problem is basically asking the minimum number of swaps to get an
        array to order. We first obtain a sorted version, and compare the
        original and the sorted arrays one element at a time. If an element is
        not the same, we look for the correct index of the element, and swap it
        there. Due to the swap, there will be a new value at the current index.
        We repeat the same process, until the current index points to the
        correct value, and then we move on.

        This produces the minimum swaps because each number takes at most two
        swaps to reach the correct position.

        O(NlogN), 1827 ms, faster than 60.52%

        NOTE: the swap part is called Cycle Sort in the discussion.
        """
        res = 0
        queue = [root]
        while queue:
            tmp = []
            lvl = []
            for node in queue:
                lvl.append(node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue = tmp
            # handle the number of swaps
            sorted_lvl = sorted(lvl)
            for i in range(len(lvl)):
                while lvl[i] != sorted_lvl[i]:
                    idx = bisect_left(sorted_lvl, lvl[i])
                    lvl[i], lvl[idx] = lvl[idx], lvl[i]
                    res += 1
        return res


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
