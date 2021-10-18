# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """LeetCode 437

        A little bit back and forth at the beginning, but we very quickly
        settled on using Counter instead of a set to record the sum of previous
        nodes in the path.

        The idea is that in order to examine whether a node can be the end of
        a path that satisfies the requirement, we need to see if the sum of the
        path from root to the current node minus the sum of the path from root
        to some of the previous node equals targetSum. In other words, we are
        looking at whether sum of the path to the current node minus targetSum
        exists in any of the previous path sums. We use a counter to keep track
        of the number of previous paths that have a specific sum. This turns the
        problem into a Two-sum problem.

        It is important to add the value from the counter, because there could
        be multiple previous path sums that satisfy the requirement, and all of
        them shall be counted.

        O(N), 44 ms, 95% ranking.
        """
        pre_sum_counter = Counter([0])
        self.res = 0

        def dfs(node: Optional[TreeNode], pre_sum: int) -> None:
            if node:
                cur_sum = node.val + pre_sum
                self.res += pre_sum_counter[cur_sum - targetSum]  # this is key
                pre_sum_counter[cur_sum] += 1
                dfs(node.left, cur_sum)
                dfs(node.right, cur_sum)
                pre_sum_counter[cur_sum] -= 1

        dfs(root, 0)
        return self.res
        


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
