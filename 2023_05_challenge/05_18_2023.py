# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        """LeetCode 1557

        A node cannot be visited from any other nodes if its indegree is zero.
        Thus, we must start from all the nodes with zero indegrees. And that is
        the answer.

        O(N + E), 1271 ms, faster than 15.02%
        """
        indegrees = Counter()
        for f, t in edges:
            indegrees[t] += 1
        return [i for i in range(n) if not indegrees[i]]


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
