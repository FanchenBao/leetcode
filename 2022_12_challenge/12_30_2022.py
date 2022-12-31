# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """LeetCode 797

        DFS, O(N), 114 ms, faster than 69.89%
        """
        N = len(graph)
        res = []
        
        def dfs(idx: int, path: List[int]) -> None:
            path.append(idx)
            if idx == N - 1:
                res.append(path[:])
            else:
                for nex in graph[idx]:
                    dfs(nex, path)
            path.pop()

        dfs(0, [])
        return res


class Solution2:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """BFS

        113 ms, faster than 70.89% 
        """
        N = len(graph)
        queue = [[0]]
        res = []
        while queue:
            tmp = []
            for path in queue:
                if path[-1] == N - 1:
                    res.append(path)
                else:
                    for nex in graph[path[-1]]:
                        tmp.append(path + [nex])
            queue = tmp
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
