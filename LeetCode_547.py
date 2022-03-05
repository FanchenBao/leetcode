# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """This is just finding the number of connected graph in the original
        graph. Use DFS to traverse each connected graph.

        O(N), 172 ms, 99% ranking.
        """
        seen = set()
        
        def dfs(i: int) -> int:
            seen.add(i)
            for j, val in enumerate(isConnected[i]):
                if val and j not in seen:
                    dfs(j)
            return 1

        return sum(dfs(i) for i in range(len(isConnected)) if i not in seen)


sol = Solution()
tests = [
    ([[1,1,0],[1,1,0],[0,0,1]], 2),
    ([[1,0,0],[0,1,0],[0,0,1]], 3),
]

for i, (isConnected, ans) in enumerate(tests):
    res = sol.findCircleNum(isConnected)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
