# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq


class Solution1:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        """Two heaps.

        O(NlogN + K) or O(KlogC), where N = len(costs), C = candidates
        1051 ms, faster than 74.46% 
        """
        N = len(costs)
        if candidates >= N:
            return sum(sorted(costs)[:k])
        lo = candidates - 1
        heap_l = [(costs[i], i) for i in range(lo + 1)]
        heapq.heapify(heap_l)
        hi = max(N - candidates, candidates)
        heap_r = [(costs[j], j) for j in range(N - 1, hi - 1, -1)]
        heapq.heapify(heap_r)
        res = 0
        while k and heap_l and heap_r:
            lc, li = heap_l[0]
            rc, ri = heap_r[0]
            if lc < rc or (lc == rc and li < ri):
                res += heapq.heappop(heap_l)[0]
                if lo + 1 < hi:
                    lo += 1
                    heapq.heappush(heap_l, (costs[lo], lo))
            else:
                res += heapq.heappop(heap_r)[0]
                if lo + 1 < hi:
                    hi -= 1
                    heapq.heappush(heap_r, (costs[hi], hi))
            k -= 1
        while k and heap_l:
            res += heapq.heappop(heap_l)[0]
            k -= 1
        while k and heap_r:
            res += heapq.heappop(heap_r)[0]
            k -= 1
        return res


class Solution2:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        """No need to record the index because if the costs are the same, we
        always want to pop the left side.

        873 ms, faster than 87.59%
        """
        N = len(costs)
        if candidates >= N:
            return sum(sorted(costs)[:k])
        lo = candidates - 1
        heap_l = [costs[i] for i in range(lo + 1)]
        heapq.heapify(heap_l)
        hi = max(N - candidates, candidates)
        heap_r = [costs[j] for j in range(N - 1, hi - 1, -1)]
        heapq.heapify(heap_r)
        res = 0
        while k:
            lc = heap_l[0] if heap_l else math.inf
            rc = heap_r[0] if heap_r else math.inf
            if lc <= rc:
                res += heapq.heappop(heap_l)
                if lo + 1 < hi:
                    lo += 1
                    heapq.heappush(heap_l, costs[lo])
            else:
                res += heapq.heappop(heap_r)
                if lo + 1 < hi:
                    hi -= 1
                    heapq.heappush(heap_r, costs[hi])
            k -= 1
        return res
        

sol = Solution2()
tests = [
    ([17,12,10,2,7,2,11,20,8], 3, 4, 11),
    ([1,2,4,1], 3, 3, 4),
]

for i, (costs, k, candidates, ans) in enumerate(tests):
    res = sol.totalCost(costs, k, candidates)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
