# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        """The most important intuition is that say we pick 0 as the root. As
        we dfs from 0 to another node, say 2. If 2 is considered the root, then
        all the parent-child order of the edges when 0 is the root are maintained
        except from the edges in the path from 0 to 2.

        Therefore, if we can compute the total number of correct guesses of
        parent-child orders when 0 is the root. We can progressively compute the
        total number of correct guesses as we traverse from 0 to all the other
        nodes. All we need to do is that each time a new node is reached, we
        check the last edge. If that last edge in its original order is in the
        guesses, then when the new node is the root, that edge will be reversed
        and won't be a correct guess. So we deduct from the total correct
        guesses. But if the reversed edge is in the guesses, then the total
        correct guesses add one.

        By doing so, we obtain the total correct guesses for each node as if it
        were the root when we reach it during DFS.

        The implementation below contains two DFS. The first one obtains the
        total number of correct guesses. And the second one progressively
        computes the correct guesses for each node.

        O(N), 2306 ms, faster than 79.81% 
        """
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        self.T = 0  # total number of correct guesses starting from some node as root
        self.res = 0
        guesses_set = set((a, b) for a, b in guesses)

        def dfs1(node: int, par: int) -> None:
            for child in graph[node]:
                if child != par:
                    self.T += int((node, child) in guesses_set)
                    dfs1(child, node)

        def dfs2(node: int, par: int, cur_correct_guesses: int) -> None:
            if cur_correct_guesses >= k:
                self.res += 1
            for child in graph[node]:
                if child != par:
                    dfs2(
                        child,
                        node,
                        cur_correct_guesses + int((child, node) in guesses_set) - int((node, child) in guesses_set),
                    )

        dfs1(0, -1)
        dfs2(0, -1, self.T)
        return self.res


sol = Solution()
tests = [
    ([[0,1],[1,2],[1,3],[4,2]], [[1,3],[0,1],[1,0],[2,4]], 3, 3),
    ([[0,1],[1,2],[2,3],[3,4]], [[1,0],[3,4],[2,1],[3,2]], 1, 5),
]

for i, (edges, guesses, k, ans) in enumerate(tests):
    res = sol.rootCount(edges, guesses, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
