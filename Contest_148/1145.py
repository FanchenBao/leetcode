#! /usr/bin/env python3
from typing import List, Dict

"""08/06/2019

Solution:
This problem took me almost two hours, because I misunderstood the problem
initially. I thought each player only had one turn, but actually they could
do multiple turns. This means eventually, the whole tree will be colored either
red of blue. Thus, the solution is simple. Since the second player can only
block one direction of the first player, we just need to see whether the
remaining two directions of the first player will amount to a value larger than
half of n. This is where "n is odd" comes into play. It guarantees that there
must be a winner. So we compute total number of nodes on first player's left,
right, and parent. Then see whether any of left + right, left + parent, or
parent + right will be smaller than n // 2. If one of them satisfies being
smaller than n // 2, then player two has a chance of win. Otherwise, player two
has no chance of winning.

There is no need for another solution, as the discussion post gives very similar
solution. However, the discussion post does provide a better return statement
and I have copied that here as well.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        left_total = [0] * (n + 1)
        right_total = [0] * (n + 1)
        self.total(root, left_total, right_total)
        return (
            max(
                left_total[x],
                right_total[x],
                n - left_total[x] - right_total[x] - 1,
            )
            > n // 2
        )

    def total(
        self, root: TreeNode, left_total: List[int], right_total: List[int]
    ) -> int:
        if not root:
            return 0
        else:
            left_total[root.val] = self.total(
                root.left, left_total, right_total
            )
            right_total[root.val] = self.total(
                root.right, left_total, right_total
            )
            return left_total[root.val] + right_total[root.val] + 1


class FunFollowUp:
    def leeWinningMoves(self, root: TreeNode, n: int, x: int) -> List[int]:
        totals: Dict[str, List[int]] = {
            "left": [0] * (n + 1),
            "right": [0] * (n + 1),
            "parent": [0] * (n + 1),
        }
        self.get_totals(root, totals, n)
        return [
            i
            for i in range(1, n + 1)
            if self.check_win(
                totals["left"][i], totals["right"][i], totals["parent"][i]
            )
        ]

    def get_totals(
        self, root: TreeNode, totals: Dict[str, List[int]], n: int
    ) -> int:
        if not root:
            return 0
        else:
            totals["left"][root.val] = self.get_totals(root.left, totals, n)
            totals["right"][root.val] = self.get_totals(root.right, totals, n)
            totals["parent"][root.val] = (
                n - totals["left"][root.val] - totals["right"][root.val] - 1
            )
            return totals["left"][root.val] + totals["right"][root.val] + 1

    def check_win(self, a: int, b: int, c: int) -> bool:
        return (a + b >= c) and (a + c >= b) and (b + c >= a)
