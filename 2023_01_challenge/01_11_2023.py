# from pudb import set_trace; set_trace()
from typing import List, Tuple


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        """LeetCode 1443

        Count the number of unique edges in all the paths that lead to an apple

        O(N) 636 ms, faster than 99.36% 
        """
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(idx, par) -> Tuple[int, bool]:
            num_paths, has_apple = 0, hasApple[idx]
            for nex in graph[idx]:
                if nex != par:
                    nex_num_paths, nex_has_apple = dfs(nex, idx)
                    num_paths += nex_num_paths + int(nex_has_apple)
                    has_apple |= nex_has_apple
            return num_paths, has_apple

        return 2 * dfs(0, -1)[0]


sol = Solution()
tests = [
    (7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,True,True,False], 8),
    (7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,False,True,False], 6),
    (7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,False,False,False,False,False], 0),
    (4, [[0,1],[1,2],[0,3]], [True,True,True,True], 6),
]

for i, (n, edges, hasApple, ans) in enumerate(tests):
    res = sol.minTime(n, edges, hasApple)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
