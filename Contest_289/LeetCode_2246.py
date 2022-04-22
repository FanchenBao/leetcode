# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def longestPath(self, parent: List[int], s: str) -> int:
        """I thought this method is called topological sort, which after I have
        read a few online articles, seems to be a minomer. Anyway, my idea is
        that we start not from the root, but from the nodes with only one
        neighbor. Each time such a node is visited, its connection to the
        neighbor is severed. Thus, each round, we will encounter new nodes with
        only one neighbor. This guarantees that the path we build is
        deterministic. Also, as we go to the neighbor, we also pass along the
        current length of the longest path that ends in the current node, if
        the letter of the current node is different from the neighbor.
        Otherwise, we don't pass anything and the neighbor has to start afresh.

        Once a node is visited, we check for all the lengths of previous nodes
        that have passed to it. We pick the two largest, and they can form a
        path with the current node being the connection. Then we pick the
        largest length as the value passing to the next neighbor.

        O(N), 3165 ms, 42.86% ranking.
        """
        N = len(parent)
        adj = [set() for _ in range(N)]
        for i in range(1, N):
            a, b = i, parent[i]
            adj[a].add(b)
            adj[b].add(a)
        res = 1
        lengths = [[0, 0] for i in range(N)]
        queue = [[i, lengths[i]] for i in range(N) if len(adj[i]) == 1]
        visited = set()
        while queue:
            temp = []
            for node, l in queue:
                l.sort()
                res = max(res, l[-1] + l[-2] + 1)
                if len(adj[node]) == 0:
                    continue
                nei = list(adj[node])[0]
                adj[nei].remove(node)
                if s[node] != s[nei]:
                    lengths[nei].append(l[-1] + 1)
                if len(adj[nei]) <= 1 and nei not in visited:
                    temp.append([nei, lengths[nei]])
                    visited.add(nei)
            queue = temp
        return res


class Solution2:
    def longestPath(self, parent: List[int], s: str) -> int:
        """DFS

        Ref: https://leetcode.com/problems/longest-path-with-different-adjacent-characters/discuss/1955433/JavaC%2B%2BPython-DFS-on-Tree

        This is essentially the same idea as Solution1, but we obviously don't
        need to use topological sort. A simple DFS suffices.

        Also, when we build the adjacency list, we can treat the graph as a DAG
        because the problem specifies that the graph is a tree (i.e. no going
        backwards).

        1736 ms, 100.00%
        """
        N = len(parent)
        adj = [[] for _ in range(N)]
        for i in range(1, N):
            adj[parent[i]].append(i)
        self.res = 1

        def dfs(node: int) -> int:
            p1, p2 = 0, 0
            for nei in adj[node]:
                p = dfs(nei)
                if s[nei] != s[node]:
                    if p > p1:
                        p1, p2 = p, p1
                    elif p > p2:
                        p2 = p
            self.res = max(self.res, p1 + p2 + 1)
            return p1 + 1

        dfs(0)
        return self.res


sol = Solution2()
tests = [
    ([-1,0,0,1,1,2], "abacbe", 3),
    ([-1,0,0,0], "aabc", 3),
    ([-1], 'z', 1),
    ([-1, 0], 'aa', 1),
    ([-1,0,1], 'aab', 2),
    ([-1,137,65,60,73,138,81,17,45,163,145,99,29,162,19,20,132,132,13,60,21,18,155,65,13,163,125,102,96,60,50,101,100,86,162,42,162,94,21,56,45,56,13,23,101,76,57,89,4,161,16,139,29,60,44,127,19,68,71,55,13,36,148,129,75,41,107,91,52,42,93,85,125,89,132,13,141,21,152,21,79,160,130,103,46,65,71,33,129,0,19,148,65,125,41,38,104,115,130,164,138,108,65,31,13,60,29,116,26,58,118,10,138,14,28,91,60,47,2,149,99,28,154,71,96,60,106,79,129,83,42,102,34,41,55,31,154,26,34,127,42,133,113,125,113,13,54,132,13,56,13,42,102,135,130,75,25,80,159,39,29,41,89,85,19],"ajunvefrdrpgxltugqqrwisyfwwtldxjgaxsbbkhvuqeoigqssefoyngykgtthpzvsxgxrqedntvsjcpdnupvqtroxmbpsdwoswxfarnixkvcimzgvrevxnxtkkovwxcjmtgqrrsqyshxbfxptuvqrytctujnzzydhpal",17),
]

for i, (parent, s, ans) in enumerate(tests):
    res = sol.longestPath(parent, s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
