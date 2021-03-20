# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """LeetCode 841

        Straightforward BFS solution. Think of the keys in each room as the
        link to the children. We traverse this tree and keep a record of all the
        nodes that we have visited before. At the end, we check the length of
        the visited node and the length of rooms. If they do not match, that
        means some room has not been visited.

        O(N), 68 ms, 52% ranking.
        """
        queue = [0]
        visited = {0}
        while queue:
            next_q = []
            for ri in queue:
                for k in rooms[ri]:
                    if k not in visited:
                        next_q.append(k)
                        visited.add(k)
            queue = next_q
        return len(visited) == len(rooms)


class Solution2:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """DFS using recursion.

        O(N), 68 ms, 52% ranking.
        """
        visited = {0}

        def dfs(ri: int):
            for k in rooms[ri]:
                if k not in visited:
                    visited.add(k)
                    dfs(k)

        dfs(0)
        return len(visited) == len(rooms)


sol = Solution2()
tests = [
    ([[1], [2], [3], []], True),
    ([[1, 3], [3, 0, 1], [2], [0]], False),
    ([[0]], True),
    ([[0], [1]], False),
]

for i, (rooms, ans) in enumerate(tests):
    res = sol.canVisitAllRooms(rooms)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
