# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """LeetCode 207

        Topological sort.

        O(M + N), where M = len(prerequisites), N = numCourses.
        117 ms, faster than 50.46%
        """
        graph = defaultdict(list)
        indegrees = [0] * numCourses
        can_take = [False] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indegrees[a] += 1
        queue = [i for i in range(numCourses) if indegrees[i] == 0]
        while queue:
            tmp = []
            for cource in queue:
                can_take[cource] = True
                for next_course in graph[cource]:
                    indegrees[next_course] -= 1
                    if indegrees[next_course] == 0:
                        tmp.append(next_course)
            queue = tmp
        return sum(can_take) == numCourses
        

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
