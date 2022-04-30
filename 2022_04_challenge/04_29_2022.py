# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """LeetCode 785

        I am pretty sure this is not the ideal solution. But basically I DFS
        the entire graph, placing current node and its neighbors into two
        separate set. Eventually I check whether the size of the two sets add
        up to the total number of nodes. One important thing to note is that
        if graph is disjoint, as long as each subgraph is bipartite, the
        overall graph must also be bipartite.

        265 ms, faster than 38.02%
        """
        N = len(graph)
        s1, s2 = set(), set()
        visited = set()
        
        def dfs(node: int) -> None:
            visited.add(node)
            if node in s1:
                for nei in graph[node]:
                    s2.add(nei)
            else:
                for nei in graph[node]:
                    s1.add(nei)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)

        for i in range(N):
            if i not in visited:
                s1.add(i)
                dfs(i)
        return len(s1) + len(s2) == N


class Solution2:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """This is the optimal solution, using coloring. The basic idea is very
        similar to Solution1, but we don't have to wait until the end to tell
        whether the graph is bipartite. We can tell while coloring the graph.
        If some coloring is wrong, then we can immediately return False.

        O(N) 182 ms, faster than 85.71%
        """
        N = len(graph)
        colors = [0] * N
        
        def dfs(node: int, color: int) -> None:
            if colors[node]:  # current node has been visited before, check color
                return colors[node] == color
            colors[node] = color
            for nei in graph[node]:
                if not dfs(nei, -color):
                    return False
            return True

        for i in range(N):
            if not colors[i] and not dfs(i, 1):
                return False
        return True


sol = Solution2()
tests = [
    ([[1,2,3],[0,2],[0,1,3],[0,2]], False),
    ([[1,3],[0,2],[1,3],[0,2]], True),
    ([[1,3],[0],[],[0]], True),
    ([[1,3],[0],[4,5],[0],[2],[2]], True),
    ([[1],[0,3],[3],[1,2]], True),
]

for i, (graph, ans) in enumerate(tests):
    res = sol.isBipartite(graph)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
