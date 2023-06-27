# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq


class Solution1:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        """LeetCode 2462

        Not really a difficult one, but I made quite a few coding issues that
        took a while to resolve.

        O(ClogC + KlogC + N), 1165 ms, faster than 9.93% 
        """
        lh, rh = [], []
        N = len(costs)
        for i in range(min(N, candidates)):
            heapq.heappush(lh, (costs[i], i))
        for j in range(N - 1, max(N - 1 - candidates, -1), -1):
            heapq.heappush(rh, (costs[j], j))
        res = 0
        lo, hi = min(N, candidates), max(N - 1 - candidates, -1)
        for _ in range(k):
            lc, i = lh[0]
            rc, j = rh[0]
            if lc < rc or (lc == rc and i < j):
                heapq.heappop(lh)
                res += lc
                costs[i] = 0
                while lo < N:
                    if costs[lo]:
                        heapq.heappush(lh, (costs[lo], lo))
                        lo += 1
                        break
                    lo += 1
            elif lc > rc or (lc == rc and i > j):
                heapq.heappop(rh)
                res += rc
                costs[j] = 0
                while hi >= 0:
                    if costs[hi]:
                        heapq.heappush(rh, (costs[hi], hi))
                        hi -= 1
                        break
                    hi -= 1
            else:  # lc == rc and i == j
                heapq.heappop(lh)
                heapq.heappop(rh)
                res += lc
                costs[i] = 0
                while lo < N:
                    if costs[lo]:
                        heapq.heappush(lh, (costs[lo], lo))
                        lo += 1
                        break
                    lo += 1
                while hi >= 0:
                    if costs[hi]:
                        heapq.heappush(rh, (costs[hi], hi))
                        hi -= 1
                        break
                    hi -= 1
        return res


class Solution2:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        """Two improvements.

        1. No need to worry about overlap. Once overlap happens, we ignore it,
        because the overlapping values must have been added to one heap already.
        There is no need to continue adding them.
        2. There is no need to include indices, because if there are identical
        costs on both heaps, we always use the left one.

        The key is DO NOT overlap.

        841 ms, faster than 63.49%
        """
        N = len(costs)
        if candidates >= N:  # this ensures no overlap in all the analysis
            return sum(sorted(costs)[:k])
        lh, rh = [], []
        for i in range(candidates):
            heapq.heappush(lh, (costs[i]))
        for j in range(N - 1, max(N - 1 - candidates, candidates - 1), -1):
            # Note that in order not to overlap, we cannot encroach the values
            # already added to lh
            heapq.heappush(rh, (costs[j]))
        res = 0
        lo, hi = candidates - 1, max(N - candidates, candidates)
        while k and lh and rh:
            if lh[0] <= rh[0]:
                res += heapq.heappop(lh)
                if lo + 1 < hi:
                    lo += 1
                    heapq.heappush(lh, costs[lo])
            else:
                res += heapq.heappop(rh)
                if lo + 1 < hi:
                    hi -= 1
                    heapq.heappush(rh, costs[hi])
            k -= 1
        while k and lh:
            res += heapq.heappop(lh)
            k -= 1
        while k and rh:
            res += heapq.heappop(rh)
            k -= 1
        return res



sol = Solution2()
tests = [
    ([17,12,10,2,7,2,11,20,8], 3, 4, 11),
    ([1,2,4,1], 3, 3, 4),
    ([17,12,10,2,7,2,11,20,8], 4, 4, 19),
    ([17,12,10,2,7,2,11,20,8], 5, 4, 29),
    ([17,12,10,2,7,2,11,20,8], 6, 4, 40),
    ([31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58], 2, 2, 42),
    ([31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58], 11, 2, 423),
    ([18,64,12,21,21,78,36,58,88,58,99,26,92,91,53,10,24,25,20,92,73,63,51,65,87,6,17,32,14,42,46,65,43,9,75], 13, 23, 223),
]

for i, (costs, k, candidates, ans) in enumerate(tests):
    res = sol.totalCost(costs, k, candidates)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
