# from pudb import set_trace; set_trace()
from typing import List, Set
import math
from collections import defaultdict, deque, Counter


class Solution1:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        """TLE
        """
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        self.visited = set()

        def dfs(node: int, clique: Set[int]) -> None:
            clique.add(node)
            self.visited.add(node)
            for nex in graph[node]:
                if nex not in clique and nex not in self.visited:
                    dfs(nex, clique)


        queue = deque([list(range(len(vals)))])
        res = len(vals)
        while queue:
            cur_nodes = queue.popleft()
            cur_nodes.sort(key=lambda i: vals[i])
            idx = cur_nodes.pop()
            nodes_to_remove = [idx]
            while cur_nodes and vals[cur_nodes[-1]] == vals[idx]:
                nodes_to_remove.append(cur_nodes.pop())
            res += math.comb(len(nodes_to_remove), 2)
            for node in nodes_to_remove:
                for child in graph[node]:
                    graph[child].remove(node)
                del graph[node]
            self.visited = set(nodes_to_remove)
            for root in cur_nodes:
                if root not in self.visited:
                    clique = set()
                    dfs(root, clique)
                    queue.append(list(clique))
        return res


class DSU:
    def __init__(self, n: int) -> None:
        self.par = list(range(n))
        self.rnk = [0] * n

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rnk[px] > self.rnk[py]:
            self.par[py] = px
        elif self.rnk[py] > self.rnk[px]:
            self.par[px] = py
        else:
            self.rnk[px] += 1
            self.par[py] = px
        return True


class Solution2:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        """Try union-find for finding the clique

        TLE
        """
        N = len(vals)
        if N == 1:
            return 1

        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        queue = deque([list(range(len(vals)))])
        res = N
        while queue:
            cur_nodes = queue.popleft()
            cur_nodes.sort(key=lambda i: vals[i], reverse=True)
            cnt = 1
            while cnt < len(cur_nodes):
                if vals[cur_nodes[cnt]] != vals[cur_nodes[cnt - 1]]:
                    break
                cnt += 1
            # print(cur_nodes, cnt)
            res += math.comb(cnt, 2)
            for i in range(cnt):
                node = cur_nodes[i]
                for child in graph[node]:
                    graph[child].remove(node)
                del graph[node]
            dsu = DSU(N)
            for i in range(cnt, len(cur_nodes)):
                node = cur_nodes[i]
                for child in graph[node]:
                    dsu.union(node, child)
            cliques = defaultdict(list)
            for i in range(cnt, len(cur_nodes)):
                node = cur_nodes[i]
                cliques[dsu.find(node)].append(node)
            for v in cliques.values():
                if len(v) > 1:
                    queue.append(v)
        return res


class Solution3:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        """Union-find again, but this time we start from small to big and build
        only one DSU.

        We first sort nodes based on their values from small to large.

        At each node, we only add edges leading to children that have values
        smaller than us.

        When the current node's value is different from the previous value, we
        go through nodes list to get all the nodes that have the same previous
        value. We then go to DSU to count how many of them belong to the same
        clique. For each clique, if there is n count of the nodes, we have
        math.comb(n, 2) new good paths.

        2522 ms, faster than 73.48%
        """
        N = len(vals)
        if N == 1:
            return 1

        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        res = N
        dsu = DSU(N)
        nodes = sorted(range(N), key=lambda i: vals[i])
        cur_val = -1
        for i, node in enumerate(nodes):
            if i > 0 and vals[node] != cur_val:
                j = i - 1
                counter = Counter()
                while j >= 0 and vals[nodes[j]] == cur_val:
                    counter[dsu.find(nodes[j])] += 1
                    j -= 1
                res += sum(math.comb(v, 2) for v in counter.values())
                cur_val = vals[node]
            for child in graph[node]:
                if vals[child] <= vals[node]:
                    dsu.union(node, child)
        # handle the last val
        j = N - 1
        counter = Counter()
        while j >= 0 and vals[nodes[j]] == cur_val:
            counter[dsu.find(nodes[j])] += 1
            j -= 1
        res += sum(math.comb(v, 2) for v in counter.values())
        return res


class Solution4:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        """This is the same solution as I submitted Oct 2, 2022

        The idea is different from Solution3. In this one, we start with an edge
        with the smallest max val of the two nodes.

        After sort, each time two nodes connect, we are always connecting with
        the largest value currently available. This means any nodes in the two
        subtree with the same largest value can be connected. For instance, we
        are connecting node a and b. The largest value between them is m. Now
        beofre a and b are connected, they are each a root of their subtree.
        Suppose subtree rooted at a has M number of nodes with value m, subtree
        rooted at b has N number of nodes with value m. The total number of
        good paths connecting nodes with value m would be M * N

        2829 ms, faster than 65.39%
        """
        # counters[i] is a counter that tells the number of nodes with a certain
        # value in the subtree rooted at i
        counters = [Counter([v]) for v in vals]
        dsu = DSU(len(vals))
        res = len(vals)
        for max_v, a, b in sorted((max(vals[a], vals[b]), a, b) for a, b in edges):
            ra, rb = dsu.find(a), dsu.find(b)
            res += counters[rb][max_v] * counters[ra][max_v]
            dsu.union(a, b)
            counters[dsu.find(a)][max_v] = counters[rb][max_v] + counters[ra][max_v]
        return res


sol = Solution4()
tests = [
    ([1,3,2,1,3], [[0,1],[0,2],[2,3],[2,4]], 6),
    ([1,1,2,2,3], [[0,1],[1,2],[2,3],[2,4]], 7),
    ([1], [], 1),
    ([2,4,1,2,2,5,3,4,4], [[0,1],[2,1],[0,3],[4,1],[4,5],[3,6],[7,5],[2,8]], 11),
]

for i, (vals, edges, ans) in enumerate(tests):
    res = sol.numberOfGoodPaths(vals, edges)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
