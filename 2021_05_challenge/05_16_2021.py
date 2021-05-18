# from pudb import set_trace; set_trace()
from typing import List, Tuple
from collections import defaultdict
import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def minCameraCover(self, root: TreeNode) -> int:
        """LeetCode 968

        There are three states a node can be in.

        0 => no camera no coverage
        1 => no camera with coverage
        2 => camera (of course with coverage)

        The idea is to compute the min number of cameras needed for the root
        of each subtree for all three states. Then the solution would be the
        min of the 0 and 2 state of the overall root.

        We can use dfs to do this, along with memoization. The tricky part is
        the 0 state, because we have to consider whether the node has left or
        right child. In the 0 state, a node must have camera either in the left
        or right child. Thus, if the node does not have left or right child, it
        must force the other child to bear camera. Of course, if the node in
        question is a leaf node, then it is impossible to be in 0 state. Thus
        we return math.inf.

        O(N^2) (this is wrong! It's O(N)), 68 ms, 6% ranking.
        """
        dp = defaultdict(lambda : [-1] * 3)

        def dfs(node: TreeNode, state: int):
            if not node:
                return 0
            if dp[node][state] < 0:
                if state == 2:
                    dp[node][state] = 1 + min(
                        dfs(node.left, 1), dfs(node.left, 2)
                    ) + min(
                        dfs(node.right, 1), dfs(node.right, 2)
                    )
                elif state == 0:
                    if node.left and node.right:
                        dp[node][state] = min(
                            dfs(node.left, 2) + min(dfs(node.right, 0), dfs(node.right, 2)),
                            min(dfs(node.left, 0), dfs(node.left, 2)) + dfs(node.right, 2),
                        )
                    elif node.left:
                        dp[node][state] = dfs(node.left, 2)
                    elif node.right:
                        dp[node][state] = dfs(node.right, 2)
                    else:
                        dp[node][state] = math.inf
                else:
                    dp[node][state] = min(
                        dfs(node.left, 0), dfs(node.left, 2)
                    ) + min(
                        dfs(node.right, 0), dfs(node.right, 2)
                    )
            return dp[node][state]

        return min(dfs(root, 0), dfs(root, 2))


class Solution2:
    def minCameraCover(self, root: TreeNode) -> int:
        """My state but with the logic in the  official solution

        0 => no camera no coverage
        1 => no camera with coverage
        2 => camera (of course with coverage)

        The difference between my states and the official solution states is
        that my state considers when we first enter a node. We want to answer
        the question of how the subtree should behavior in order to reconsile
        with my state. Therefore, my 0 state requires at least one of my
        children to have camera.

        Apparently, we not need to use external memoization. And the runtime is
        actually O(N), not O(N^2).
        """

        def dfs(node: TreeNode) -> Tuple:
            if not node:
                return 0, 0, math.inf
            L = dfs(node.left)
            R = dfs(node.right)
            s0 = min(L[2] + min(R[0], R[2]), R[2] + min(L[0], L[2]))
            s1 = min(L[0], L[2]) + min(R[0], R[2])
            s2 = 1 + min(L[1], L[2]) + min(R[1], R[2])
            return s0, s1, s2

        res = dfs(root)
        return min(res[0], res[2])





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
