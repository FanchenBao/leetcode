# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """LeetCode 841

        The graph has already been created in `rooms`. No need to generate a new
        one.

        O(N), 138 ms, faster than 53.23%
        """
        visited = [0] * len(rooms)

        def dfs(room: int) -> None:
            if not visited[room]:
                visited[room] = 1
                for nex in rooms[room]:
                    dfs(nex)

        dfs(0)
        return sum(visited) == len(rooms)

        

sol = Solution()
tests = [
    ([[1],[2],[3],[]], True),
    ([[1,3],[3,0,1],[2],[0]], False),
]

for i, (rooms, ans) in enumerate(tests):
    res = sol.canVisitAllRooms(rooms)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
