# from pudb import set_trace; set_trace()
from typing import List, Tuple
import math
from collections import Counter

GraphT = List[List[Tuple[int, int]]]
AncMatT = List[List[int]]
PathFreqsT = List[Counter]


class Solution:
    def kth_ancestor(self, node: int, k: int, anc_mat: AncMatT) -> int:
        anc = node
        idx = 0
        while k:
            if k & 1:
                anc = anc_mat[anc][idx]
            idx += 1
            k >>= 1
        return anc

    def gen_anc_matrix(
        self,
        node: int,
        par: int,
        lvl: int,
        graph: GraphT,
        anc_mat: AncMatT,
        levels: List[int],
    ) -> None:
        levels[node] = lvl
        anc_mat[node].append(par)  # the 2^0 th ancestor of node is parent
        i = 1
        while (1 << i) <= lvl:
            anc = anc_mat[anc_mat[node][i - 1]][i - 1]
            anc_mat[node].append(anc)
            i += 1
        for child, _ in graph[node]:
            if child != par:
                self.gen_anc_matrix(child, node, lvl + 1, graph, anc_mat, levels)

    def get_lca(self, n1: int, n2: int, anc_mat: AncMatT, levels: List[int]) -> int:
        """
        Find the lowest common ancestor of the given two nodes
        """
        if levels[n1] > levels[n2]:
            n1, n2 = n2, n1
        n2 = self.kth_ancestor(n2, levels[n2] - levels[n1], anc_mat)
        if n1 == n2:
            return n1
        lvl = levels[n1]
        while lvl > 0:
            a1, a2 = (
                self.kth_ancestor(n1, lvl, anc_mat),
                self.kth_ancestor(n2, lvl, anc_mat),
            )
            if a1 == a2:
                lvl -= 1
            else:
                lvl = min(levels[a1], levels[a2]) - 1
                n1, n2 = a1, a2
        return anc_mat[n1][0]

    def gen_path_freq(
        self,
        node: int,
        par: int,
        graph: GraphT,
        weight_freqs: PathFreqsT,
        cur_freq: Counter,
    ) -> None:
        weight_freqs[node] = cur_freq.copy()
        for child, weight in graph[node]:
            if child != par:
                cur_freq[weight] += 1
                self.gen_path_freq(child, node, graph, weight_freqs, cur_freq)
                cur_freq[weight] -= 1

    def minOperationsQueries(
        self, n: int, edges: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        """
        Failed.

        Cannot solve this problem without going through the hints. Also, it
        is pretty much impossible to implement the LCA algorithm from scratch
        without any help.

        Basically, we DFS the tree from any node, and produce a weight frequency
        for each node during DFS. Then we can obtain the weight frequency from
        the path between any two nodes by performing source weight frequency
        + destinatin weight frequency - 2 * lca weight frequency, where lca
        is the lowest common ancestor of source and destination. Then the
        answer to the source-destination pair is the total number of edges
        minus the most common count of weights.

        The most difficult part of this algorithm is undoubtedly the LCA. I
        need a lot of help to implement the LCA using binary lifting.
        """
        graph: GraphT = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        # generate ancestor matrix
        anc_mat: AncMatT = [[] for _ in range(n)]
        levels = [0] * n
        self.gen_anc_matrix(0, 0, 0, graph, anc_mat, levels)

        # generate the frequency of the path to each node
        weight_freqs: PathFreqsT = [Counter() for _ in range(n)]
        self.gen_path_freq(0, 0, graph, weight_freqs, Counter())

        res = []
        for s, d in queries:
            lca = self.get_lca(s, d, anc_mat, levels)
            pf = (
                weight_freqs[s]
                + weight_freqs[d]
                - weight_freqs[lca]
                - weight_freqs[lca]
            )
            res.append(sum(pf.values()) - pf.most_common(1)[0][1])
        return res


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
