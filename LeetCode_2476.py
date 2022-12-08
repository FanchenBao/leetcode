# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_right


class Solution1:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        """TLE, because the binary search tree can be lopsided.
        """
        def q1(node: Optional[TreeNode], tgt: int) -> int:
            if not node:
                return -1
            if node.val == tgt:
                return tgt
            if node.val > tgt:
                return q1(node.left, tgt)
            res = q1(node.right, tgt)
            if res == -1:
                return node.val
            return res

        def q2(node: Optional[TreeNode], tgt: int) -> int:
            if not node:
                return -1
            if node.val == tgt:
                return tgt
            if node.val < tgt:
                return q2(node.right, tgt)
            res = q2(node.left, tgt)
            if res == -1:
                return node.val
            return res

        res = []
        for q in queries:
            res.append([q1(root, q), q2(root, q)])
        return res


class Solution2:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        """Feels like a cheat. We turn the binary search tree into a sorted arr
        and then binary search it.

        O(N + MlogN), where N is the total number of nodes and M = len(queries)
        """
        arr = []

        def dfs(node: Optional[TreeNode]) -> None:
            if node:
                dfs(node.left)
                arr.append(node.val)
                dfs(node.right)

        dfs(root)
        res = []
        for q in queries:
            i = bisect_right(arr, q)
            if i == 0:
                res.append([-1, arr[0]])
            elif arr[i - 1] == q:  # this has to be checked before i == len(arr), because q == arr[-1] also fits this
                res.append([q, q])
            elif i == len(arr):
                res.append([arr[-1], -1])
            else:
                res.append([arr[i - 1], arr[i]])
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
