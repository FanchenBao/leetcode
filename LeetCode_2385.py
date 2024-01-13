
# from pudb import set_trace; set_trace()
from typing import List, Optional, Tuple
import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        """
        This solution comes from the official solution, in which we find the
        amount of time in one pass and without altering the original binary
        tree.

        The main trick is to report the depth from any ancestor to the start
        node and differentiate that from the regular depth of the ancestor
        node. The official solution uses a negative number to represent the
        depth from any ancestor of start to the start node. By identifying this
        depth, we are able to compute the time it will take for the infection
        to go through from the start to the ancestor (this is the negative
        depth) and from the ancestor down through its subtree that does not
        contain the start node.

        Very very smart solution. And that also makes this problem a good
        candidate for interview.
        """
        self.res = 0

        def depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            ld = depth(node.left)
            rd = depth(node.right)
            if ld >= 0 and rd >= 0:
                # this is the case of a subtree that does not contain start
                return max(ld, rd) + 1
            if node.val == start:
                self.res = max(self.res, ld, rd)
                return -1  # this is the trick
            # the next case is an ancestor with one subtree containing start
            # one of the abs(ld) or abs(rd) is the distance from the ancestor
            # towards the start node
            self.res = max(self.res, abs(ld) + abs(rd) + 1)
            # for ancestors whose subtree contains the start node, what we are
            # interested in is to return the distance from the ancestor to
            # the start node
            return min(ld, rd) - 1

        depth(root)
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
