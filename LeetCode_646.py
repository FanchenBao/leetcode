# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        """Another greedy problem. We sort pairs by the end of each interval.
        Each time we try to pick the interval with the smallest end. This way
        we always leave the max room to include other intervals.

        O(NlogN), 212 ms, 93% ranking.
        """
        pairs.sort(key=lambda p: p[1])
        res = 0
        pre = -math.inf
        for pl, pr in pairs:
            if pl > pre:
                res += 1
                pre = pr
        return res


sol = Solution()
tests = [
    ([[1,2],[2,3],[3,4]], 2),
    ([[1,2],[7,8],[4,5]], 3),
]

for i, (pairs, ans) in enumerate(tests):
    res = sol.findLongestChain(pairs)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
