# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter
import math


class Solution1:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        """LeetCode 1007

        We first use counter on tops and bottoms. Then we check tiles 1 to 6.
        For each tile, we first check whether the total number of occurrences
        of the tile is larger or equal to len(tops). If not, this tile cannot
        fill all top or all bottom. If the number is larger or equal to
        len(tops), then we check whether coverage is possible. We iterate
        through all positions and keep count of how many missing spots there
        are on top and bottom. If at any position, neither top or bottom has
        the current tile, the current tile cannot cover. Otherwise, after
        confirming that the current tile can cover top or bottom, we compare
        the number of swaps needed if bottom swaps to top or the other way
        around.

        O(6N), 1858 ms, 21% ranking.
        """
        topc = Counter(tops)
        botc = Counter(bottoms)
        N = len(tops)
        res = math.inf
        for t in range(1, 7):
            if topc[t] + botc[t] < N:
                continue
            mis_top = mis_bot = 0
            for i in range(N):
                if tops[i] != t and bottoms[i] == t:
                    mis_top += 1
                if tops[i] == t and bottoms[i] != t:
                    mis_bot += 1
                if tops[i] != t and bottoms[i] != t:
                    break
            else:
                res = min(res, min(mis_top, topc[t]), min(mis_bot, botc[t]))
        return -1 if res == math.inf else res


class Solution2:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        """This solution is from the one submitted on 2020-10-19.

        The key observation is that to make the swap work, the tops and bottoms
        must confirm to either tops[0] and bottoms[0]. Thus, these are the only
        two values that need to check.
        """
        topc = Counter(tops)
        botc = Counter(bottoms)
        N = len(tops)
        res = math.inf
        for t in set([tops[0], bottoms[0]]):  # only consider two values
            if topc[t] + botc[t] < N:
                continue
            mis_top = mis_bot = 0
            for i in range(N):
                if tops[i] != t and bottoms[i] == t:
                    mis_top += 1
                if tops[i] == t and bottoms[i] != t:
                    mis_bot += 1
                if tops[i] != t and bottoms[i] != t:
                    break
            else:
                res = min(res, min(mis_top, topc[t]), min(mis_bot, botc[t]))
        return -1 if res == math.inf else res



sol = Solution2()
tests = [
    ([2,1,2,4,2,2], [5,2,6,2,3,2], 2),
    ([3,5,1,2,3], [3,6,3,3,4], -1),
    ([1,2,1,1,1,2,2,2], [2,1,2,2,2,2,2,2], 1),
]

for i, (tops, bottoms, ans) in enumerate(tests):
    res = sol.minDominoRotations(tops, bottoms)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
