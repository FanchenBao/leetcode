# from pudb import set_trace; set_trace()
from typing import List, Optional
from itertools import product
from functools import lru_cache


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        """LeetCode 95

        This problem looks quite challenging as it requires us to produce all
        valid BST given an input n. However, it can be solved elegantly with
        recursion. The idea is that we can pick any value v from a given range
        [lo, hi]. Then we produce all possible BST from [lo, v - 1] as potential
        left subtrees, and from [v + 1, hi] as potential right subtrees. After
        that, we mix and match all the subtrees from left and right, and add
        them to the root node specified by v.

        I am troubled by figuring out the time complexity.

        85 ms, 11% ranking.

        UDATE: regarding the time complexity, refer to this:

        https://leetcode.com/problems/unique-binary-search-trees-ii/discuss/1440128/Python-DFS-with-Memoization-Clean-and-Concise

        Catalan number Cn is the number of unique BST given a sequence of n
        numbers.
        """

        @lru_cache(None)
        def helper(lo: int, hi: int) -> List[Optional[TreeNode]]:
            if lo > hi:
                return [None]
            res = []
            for val in range(lo, hi + 1):
                for left, right in product(helper(lo, val - 1), helper(val + 1, hi)):
                    res.append(TreeNode(val=val, left=left, right=right))
            return res

        return helper(1, n)


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
