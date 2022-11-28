# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        """LeetCode 2225

        Use counter.

        O(NlogN), 3450 ms, faster than 68.51%

        UPDATE: we only need one counter.
        2076 ms, faster than 83.99%
        """
        lc = Counter()
        for w, l in matches:
            lc[w] += 0
            lc[l] += 1
        res = [[], []]
        for player in lc:
            if lc[player] == 0:
                res[0].append(player)
            elif lc[player] == 1:
                res[1].append(player)
        res[0].sort()
        res[1].sort()
        return res


sol = Solution()
tests = [
    ([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]], [[1,2,10],[4,5,7,8]]),
    ([[2,3],[1,3],[5,4],[6,4]], [[1,2,5,6],[]]),
]

for i, (matches, ans) in enumerate(tests):
    res = sol.findWinners(matches)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
