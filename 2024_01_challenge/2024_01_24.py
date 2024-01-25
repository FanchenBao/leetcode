# from pudb import set_trace; set_trace()
from typing import List, Optional
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        """
        LeetCode 1457

        DFS to each leaf and keep track of the parity of the nodes along the
        way. As long as we have at most one value whose parity is odd, we have
        a pseudo-palindromic path.

        To keep track of the parity, we can use a bit mask, where the presence
        of each value will be XORed. Thus at the end, if the bit position is
        1, we know there has been odd number of occurrences of the value.
        Otherwise, there has been even number of ocurrences.

        O(N), 332 ms, faster than 98.67%
        """
        self.res = 0
        
        def dfs(node: Optional[TreeNode], state: int) -> None:
            if not node:
                return
            new_state = state ^ (1 << node.val)
            if not node.left and not node.right:
                # we are at leaf
                if new_state.bit_count() <= 1:
                    self.res += 1
            else:
                dfs(node.left, new_state)
                dfs(node.right, new_state)

        dfs(root, 0)
        return self.res



sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
