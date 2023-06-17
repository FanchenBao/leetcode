# from pudb import set_trace; set_trace()
from typing import List, Tuple
import math


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        """LeetCode 1569

        The most difficult part is to understand the problem. Once that is done,
        the divide and conquer hint was helpful. But the most important insight
        is that the left subtree can be considered independelty from the right
        subtree, because everything on the left is smaller than everything on
        the right. Thus, the problem is converted to given N empty spaces, we
        have k values to insert first and these k values have certain number of
        ways to arrange themselves. Then we insert the remaining N - k values
        which also have their certain number of ways of arrangement. The ways
        to insert the first k values is NCk multiplied by the number of ways to
        arrange those k values. Then we multiply on top of that the number of
        ways to arrange the remaining N - k values to reach the total number of
        ways to construct both subtrees.

        O(NlogN + logN * combination), 195 ms, faster than 35.87%
        """
        root = Node(nums[0])
        for n in nums[1:]:
            node = root
            while True:
                if n < node.val:
                    if node.left:
                        node = node.left
                    else:
                        node.left = Node(n)
                        break
                else:
                    if node.right:
                        node = node.right
                    else:
                        node.right = Node(n)
                        break
        MOD = 10**9 + 7

        def solve(node: Node) -> Tuple[int, int]:  # return (num of ways, node counts)
            if not node:
                return 1, 0
            lw, lc = solve(node.left)
            rw, rc = solve(node.right)
            return (math.comb(lc + rc, lc) * lw * rw) % MOD, lc + rc + 1

        return (solve(root)[0] - 1) % MOD


sol = Solution()
tests = [
    ([2,1,3], 1),
    ([3,4,5,1,2], 5),
    ([1,2,3], 0),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.numOfWays(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
