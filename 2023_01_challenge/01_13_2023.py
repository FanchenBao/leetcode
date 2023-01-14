# from pudb import set_trace; set_trace()
from typing import List, Tuple
import math


class Solution1:
    def longestPath(self, parent: List[int], s: str) -> int:
        """LeetCode 2246

        I am glad that this solution was almost exactly the same as the updated
        one last time I encountered this problem in April 2022.

        Direct DFS. The return of dfs(idx) is the longest path that satisfies
        the question starting from idx. For each idx, we can also compute a
        potential result, which is the longest path of its child plus the second
        longest path of its child plus one.

        O(NlogN), 1829 ms, faster than 83.81% 
        """
        graph = [[] for _ in range(len(s))]
        for i, p in enumerate(parent[1:], 1):
            graph[p].append(i)
        self.res = 0

        def dfs(idx) -> int:
            max_lens = [0, 0]
            for nex in graph[idx]:
                l = dfs(nex)
                if s[nex] != s[idx]:
                    max_lens.append(l)
            max_lens.sort()
            self.res = max(self.res, max_lens[-1] + 1 + max_lens[-2])
            return max_lens[-1] + 1

        dfs(0)
        return self.res


class Solution2:
    def longestPath(self, parent: List[int], s: str) -> int:
        """Remove the sort. Use two variables to keep track the largest and
        second largest.

        O(N), 1589 ms, faster than 95.34%
        """
        graph = [[] for _ in range(len(s))]
        for i, p in enumerate(parent[1:], 1):
            graph[p].append(i)
        self.res = 0

        def dfs(idx) -> int:
            l1, l2 = 0, 0  # max, second max
            for nex in graph[idx]:
                l = dfs(nex)
                if s[nex] != s[idx]:
                    if l > l1:
                        l2, l1 = l1, l
                    elif l > l2:
                        l2 = l
            self.res = max(self.res, l1 + l2 + 1)
            return l1 + 1

        dfs(0)
        return self.res
        

sol = Solution2()
tests = [
    ([-1,0,0,1,1,2], "abacbe", 3),
    ([-1,0,0,0], "aabc", 3),
    ([-1,0,1], "aab", 2),
]

for i, (parent, s, ans) in enumerate(tests):
    res = sol.longestPath(parent, s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
