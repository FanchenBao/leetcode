#! /usr/bin/env python3
""" 07/22/2019

This is such a difficult yet FUN dynamic programming problem. I spent one hour
and half solving this problem, but it was totally worth it. I don't have time
today to write up my whole thought process. I will do that tomorrow.

Update 07/23/2019

Here is the "next day" update on Solution1. It is a DP solution with three
layers of for loop. The basic thought process can be demonstrated with this
example. Given arr = [1, 2, 3, 4], we can build all possible trees bottom up.
If we have only one leaf node, we can represent the max_leaf and min_sum value
as (1, 0), (2, 0), (3, 0), and (4, 0). If we have two leaf nodes, say [1, 2],
then there is only one way to build its tree with 1 and 2 both being the leaves.
Thus the representation of leaf nodes 1 and 2 is (2, 2). Similarly, for leaf
nodes 2 and 3, we have (3, 6), etc. At this point, we can notice that it is
possible to use a two-dimensional array to point to each such leaf combinations.
We say dp[i][j] is the representation of the leaf nodes from arr[i] to arr[j].
Thus we have dp[0][0] = (1, 0); dp[1][1] = (2, 0); dp[2][2] = (3, 0); dp[3][3]
= (4, 0); dp[0][1] = (2, 2); and dp[1][2] = (3, 6); etc.

Then we can consider three leaves, such as dp[0][2]. To compute dp[0][2], the
leaf nodes can be combined as dp[0][0] with dp[1][2], or dp[0][1] with dp[2][2].
We compute the outcome of both situations, and take one with the smaller min_sum
to assign to dp[0][2] = (3, 8).

Similarly for four leaves, dp[0][3], it can be computed as
dp[0][0] with dp[1][3]
dp[0][1] with dp[2][3]
dp[0][2] with dp[3][3]
And we pick the one with the smallest min_sum. The final returned result will
be do[0][3][1].


Update 07/24/2019

Solution2 is based on "https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/339959/One-Pass-O(N)-Time-and-Space".
I recommend myself to go to that post again in the future if I forget how this
problem is solved. A one-pass solution, utilizing the key insight that the
truth of forming the tree is to find two adjacent leaf nodes, remove the
smallest, and maintain the total cost the least. For each leaf, we just need to
find the first leaf on the right and the first leaf on the left that is bigger
than itself, pick the smaller of the two big leafs, and use that to remove our
target leaf. The catch is the left and right leaf must be adjacent to the
target leaf, due to the binary tree requirement. Thus, for any leaf node without
two big leaves on its either side, they have to be pushed into a stack and wait
for the result of the remaining leaf nodes to condense before they can be
removed. The code in the discussion post was much better than mine, but I will
leave mine here just for the sake of it.

"""
from typing import List, Tuple, Deque
from collections import deque


class Solution1:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        size = len(arr)
        # the dp[i][j] = (max_leaf, min_sum) of all the trees built
        # from the elements from arr[i] to arr[j]
        dp: List[List[Tuple[int, int]]] = [
            [(0, 0)] * size for i in range(size)
        ]
        for i, a in enumerate(arr):
            dp[i][i] = (a, 0)
        for length in range(2, size + 1):
            for i in range(size - length + 1):
                max_leaf = 0
                min_sum = 2 ** 31 - 1
                for j in range(i + 1, i + length):
                    max_left, sum_left = dp[i][j - 1]
                    max_right, sum_right = dp[j][i + length - 1]
                    max_leaf = max(max_leaf, max_left, max_right)
                    min_sum = min(
                        min_sum, sum_left + sum_right + max_left * max_right
                    )
                dp[i][j] = (max_leaf, min_sum)
        return dp[0][size - 1][1]


class Solution2:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        MAX: int = 2 ** 31 - 1
        stack: Deque[int] = deque()
        stack.append(MAX)  # dummy value
        arr.append(MAX)  # dummy value
        i = 0
        cost = 0
        while i < len(arr) - 1 and not (
            arr[i + 1] == MAX and stack[-1] == MAX
        ):
            curr = arr[i]
            if arr[i + 1] >= curr and stack[-1] >= curr:
                if arr[i + 1] <= stack[-1]:  # pick arr[i + 1]
                    cost += curr * arr[i + 1]
                    i += 1
                else:  # pick stack[-1]
                    temp = stack.pop()
                    cost += curr * temp
                    arr[i] = temp
            else:
                stack.append(curr)
                i += 1
        return cost


sol = Solution2()
print(sol.mctFromLeafValues([6, 2, 4, 3, 2, 6, 0, 0, 1, 1, 4, 5]))
