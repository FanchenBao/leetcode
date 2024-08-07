# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        """
        Use Floyd-Warshall.

        O(E + V), 1888 ms, faster than 28.57%
        """
        dists = [[math.inf] * 26 for _ in range(26)]
        for i in range(26):
            dists[i][i] = 0
        for oi, ch, co in zip(original, changed, cost):
            i, j = ord(oi) - 97, ord(ch) - 97
            dists[i][j] = min(dists[i][j], co)
        # Floyd-Warshall to find the minimum dist from any pair of letters
        for k in range(26):
            for u in range(26):
                for v in range(26):
                    dists[u][v] = min(dists[u][v], dists[u][k] + dists[k][v])
        res = 0
        for s, t in zip(source, target):
            i, j = ord(s) - 97, ord(t) - 97
            if dists[i][j] == math.inf:
                return -1
            res += int(dists[i][j])
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
