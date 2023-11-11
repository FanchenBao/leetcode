# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict
from functools import lru_cache


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        """DFS from any course to find the max time it will take to complete the
        course. The answer is the longest time to finish any single course.

        O(V + E), 1426 ms, faster than 56.81%
        """
        graph = defaultdict(list)
        for a, b in relations:
            graph[a - 1].append(b - 1)

        @lru_cache(maxsize=None)
        def dfs(node: int) -> int:
            t = 0
            for child in graph[node]:
                t = max(t, dfs(child))
            return t + time[node]

        return max(dfs(node) for node in range(n))


        

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
