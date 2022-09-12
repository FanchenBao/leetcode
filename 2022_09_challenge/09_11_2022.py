# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq


class Solution1:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        """LeetCode 1383

        Still struggled, but I was able to figure out the general process. I
        knew that if we fix the lowest efficient engineer, all we need to do
        is to find the k - 1 engineers with the largest speed that have higher
        efficiency than the lowest efficient one. Now the problem is to find
        the k - 1 max speed in any given array. I was stuck at this step.

        The solution, which I checked from my previous attempt is that we go
        from high efficiency to low. Thus we run a heap of size k - 1, which
        keeps the highest k - 1 speed seen so far. Each time a new engineer is
        encountered, we compare that to the top of the heap (min heap). If the
        new engineer has larger speed than the smallest speed in the heap, we
        swap them. We also keep track of the sum of the top k - 1 speed. This
        way, each swap incurrs O(1) time to recompute the sum.

        O(NlogK) 1060 ms, faster than 5.49%
        """
        combined = sorted(zip(efficiency, speed), reverse=True)
        heap = []
        res, comb_sum = 0, 0
        for e, s in combined:
            # we have to keep track when the number of enigneers is smaller
            # than k
            res = max(res, (comb_sum + s) * e)
            if len(heap) < k - 1:
                comb_sum += s
                heapq.heappush(heap, s)
            elif heap and heap[0] < s:
                comb_sum += s - heapq.heappop(heap)
                heapq.heappush(heap, s)
        return res % (10**9 + 7)


class Solution2:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        """This is an interesting twist. We don't have to check heap[0] < s;
        we can directly pop heap and push s. This is because if heap[0] is
        indeed smaller than s, it works. Otherwise, we know that heap[0] has
        already been involved in the previous computation with an efficiency
        not smaller than the current efficiency. This means, we have already
        generated a result with the previous efficiency that is not smaller
        than the result generated from the current efficiency even if we do
        not swap out heap[0]. Hence, although we won't get the biggest result
        at each efficiency if we swap heap[0] every single time, it is
        guaranteed that the largest result will have always been encountered.

        898 ms, faster than 13.51%
        """
        combined = sorted(zip(efficiency, speed), reverse=True)
        heap = []
        res, comb_sum = 0, 0
        for e, s in combined:
            heapq.heappush(heap, s)  # always push, regardless of value of s
            comb_sum += s
            if len(heap) > k:
                comb_sum -= heapq.heappop(heap)
            res = max(res, comb_sum * e)
        return res % 1000000007


sol = Solution2()
tests = [
    (6, [2,10,3,1,5,8], [5,4,3,9,7,2], 2, 60),
    (6, [2,10,3,1,5,8], [5,4,3,9,7,2], 3, 68),
    (6, [2,10,3,1,5,8], [5,4,3,9,7,2], 4, 72),
    (3, [2,8,2], [2,7,1], 2, 56),
]

for i, (n, speed, efficiency, k, ans) in enumerate(tests):
    res = sol.maxPerformance(n, speed, efficiency, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
