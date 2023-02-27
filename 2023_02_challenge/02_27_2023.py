# from pudb import set_trace; set_trace()
from typing import List
import math


"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> Node:
        """LeetCode 427

        Very straightforward recursion solution.

        O(N^2), because each cell is visited at most once. 125 ms, faster than 46.28%
        """

        def helper(i: int, j: int, l: int) -> Node:
            if l == 1:
                return Node(grid[i][j], True, None, None, None, None)
            tl = helper(i, j, l // 2)
            tr = helper(i, j + l // 2, l // 2)
            bl = helper(i + l // 2, j, l // 2)
            br = helper(i + l // 2, j + l // 2, l // 2)
            if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and tl.val == tr.val == bl.val == br.val:
                return Node(tl.val, True, None, None, None, None)
            return Node(1, False, tl, tr, bl, br)
        
        return helper(0, 0, len(grid))


        

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
