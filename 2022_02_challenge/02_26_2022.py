# from pudb import set_trace; set_trace()
from typing import List, Tuple
import math
from functools import lru_cache
from itertools import combinations


class Solution1:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        """LeetCode 847

        Very difficult. I wasn't able to solve it by myself. As already noted
        in the dfs function, the DP is quite tricky for top-down method.

        O(2^N * N^2), 596 ms, 34% ranking
        """
        N = len(graph)
        dp = [[-1] * (1 << N) for _ in range(N)]

        def dfs(last_node: int, target_state: int) -> int:
            """dfs(last_node, target_state) returns the shortest path from the
            state where no node is visited to the target_state where last_node
            is the last one visited in order to reach target_state. This way,
            all the neighbors of last_node are the second last node. There are
            two possibilities for the target state of last_node's neighbor.
            Either last_node has not been visited when the neighbor is visited
            (this means the current visit to the last_node is the first time
            last_node is visited), or last_node has already been visited when
            the neighbor is visited (this means the step from the neighbor to
            the last_node is a return trip). Then the shortest path to reach
            target_state with last_node being the last node is the min of the
            two situations for each of last_node's neighbor.

            The anchor case is when target_state has only one '1' in its binary
            state (and by design, this '1' must represent last_node). This case
            asks how many steps needed to go from the very beginning to
            last_node being the only node visited. The answer is obviously 0.

            This is indeed a very tricky and hard-to-reason DP relation.
            """
            if dp[last_node][target_state] >= 0:
                return dp[last_node][target_state]
            if target_state ^ (1 << last_node) == 0:
                dp[last_node][target_state] = 0
                return 0
            dp[last_node][target_state] = math.inf
            for nei in graph[last_node]:
                if (target_state >> nei) & 1:  # second last node, must be visited already
                    dp[last_node][target_state] = min(
                        dp[last_node][target_state],
                        1 + dfs(nei, target_state),  # last_node visited already
                        1 + dfs(nei, target_state ^ (1 << last_node)),  # first time visit last_node
                    )
            return dp[last_node][target_state]

        return min(dfs(r, (1 << N) - 1) for r in range(N))


class Solution2:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        """BFS. The key is to recognize that there is no restriction on
        visiting a neighbor whether the neighbor has been visited before. The
        restriction is on the tuple (cur, state). If (cur, state) has been
        seen before, we don't visit it again. Essentially, we are trying to
        visit all (cur, state), instead of all state as in the case of regular
        BFS.

        O(2^N * N^2), 184 ms, 93% ranking.
        """
        N = len(graph)
        if N == 1:
            return 0
        seen = set()
        queue = [(node, 1 << node) for node in range(N)]
        steps = -1
        while queue:
            temp = []
            steps += 1
            for node, state in queue:
                if state == (1 << N) - 1:
                    return steps
                for nei in graph[node]:
                    next_state = state | (1 << nei)
                    if (nei, next_state) not in seen:
                        seen.add((nei, next_state))
                        temp.append((nei, next_state))
            queue = temp
 

sol = Solution2()
tests = [
    ([[1,2,3],[0],[0],[0]], 4),
    ([[1],[0,2,4],[1,3,4],[2],[1,2]], 4),
    ([[]], 0),
    ([[1], [0]], 1),
    ([[1,2,3,4],[0,2],[0,1],[0,5],[0,6],[3],[4]], 7),
]

for i, (graph, ans) in enumerate(tests):
    res = sol.shortestPathLength(graph)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
