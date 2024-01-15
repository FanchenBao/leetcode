# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        """
        LeetCode 2225

        Create a graph and find the nodes with 0 or 1 indegrees

        O(N + MlogM), where N = len(matches) and M is the total number of
        players.

        1470 ms, faster than 74.72%
        """
        indegrees = Counter()
        for w, l in matches:
            indegrees[w] += 0
            indegrees[l] += 1
        res = [[], []]
        for k, v in indegrees.items():
            if v <= 1:
                res[v].append(k)
        res[0].sort()
        res[1].sort()
        return res



sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
