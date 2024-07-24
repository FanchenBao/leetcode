# from pudb import set_trace; set_trace()
from typing import List, Tuple
import math
from collections import Counter

GraphT = List[List[Tuple[int, int]]]
AncMatT = List[List[int]]
PathFreqsT = List[Counter]


class Solution:
    def kth_ancestor(self, node: int, k: int, graph: GraphT, anc_mat: AncMatT) -> int:
        pass

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

    def gen_path_freq(
        self,
        node: int,
        par: int,
        graph: GraphT,
        path_freqs: PathFreqsT,
        cur_freq: Counter,
    ) -> None:
        path_freqs[node] = cur_freq.copy()
        for child, weight in graph[node]:
            if child != par:
                cur_freq[weight] += 1
                self.gen_path_freq(child, node, graph, path_freqs, cur_freq)
                cur_freq[weight] -= 1

    def minOperationsQueries(
        self, n: int, edges: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        graph: GraphT = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        # generate ancestor matrix
        anc_mat: AncMatT = [[] for _ in range(n)]
        levels = [0] * n
        self.gen_anc_matrix(0, 0, 0, graph, anc_mat, levels)

        # generate the frequency of the path to each node
        path_freqs: PathFreqsT = [Counter() for _ in range(n)]
        self.gen_path_freq(0, 0, graph, path_freqs, Counter())


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
