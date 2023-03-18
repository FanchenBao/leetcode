# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter
import heapq
from bisect import bisect_right


class Solution1:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        """We can use a counter to find all the unique positions in order.
        If the two segments can cover the entire range of positions, then we
        shall include all prizes. To check this, let's say the smallest position
        is minP and the largest position is maxP. If minP + k + 1 + k >= maxP,
        then the two segments can cover the entire range. We are done.

        If two segments cannot cover, then we want to compute all the segments
        starting from each position that has prize. Then, for each such segment,
        we shall find the largest segment that does not overlap with it. To
        find such largest segment, we can use a heap.

        For instance, given [1,1,2,2,3,3,4,4,4,5,5,5,6,6,6,7,7,8,8], and k = 2
        we have the following list of all segment sums
        
        [6,7,8,9,8,7,4,2]

        where 6 = sum of range 1-3, 7 = sum of range 2-4, etc.

        Then, if we pick range 1-3, we need to find the max rang sum from 4 to
        the end. This means we need to create a heap with [9, 8, 7, 4, 2]. The
        largest is 9, thus the max that we can reach with 1-3 selected is 6 + 9
        = 15.

        Then we move on to the next one, and we pop heap if the range at the top
        overlaps with the current range in consideration.

        Keep doing this until we exhaust the heap.

        O(NlogN), 675 ms, faster than 92.78%
        """
        counter = Counter(prizePositions)
        pos = list(counter.keys())
        if pos[0] + 2 * k + 1 >= pos[-1]:
            return sum(counter.values())
        
        N = len(pos)
        lst = []
        hi = 0
        for lo, p in enumerate(pos):
            cur = 0 if not lst else lst[-1] - counter[pos[lo - 1]]
            while hi < len(pos) and pos[hi] <= p + k:
                cur += counter[pos[hi]]
                hi += 1
            lst.append(cur)
        
        # print(lst, pos)
        idx = bisect_right(pos, pos[0] + k)
        heap = []
        for i in range(idx, N):
            heapq.heappush(heap, (-lst[i], pos[i]))
        res = -1
        for i in range(N):
            while heap and pos[i] + k >= heap[0][1]:
                heapq.heappop(heap)
            if not heap:
                break
            res = max(res, lst[i] - heap[0][0])
        return res


class Solution2:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        """This is lee215's O(N) solution.

        ref: https://leetcode.com/problems/maximize-win-from-two-segments/discuss/3141449/JavaC%2B%2BPython-DP-%2B-Sliding-Segment-O(n)

        Use DP. Let dp[i] be the max segment in range prizePositions[:i + 1]

        Then for a current range ending at prizePositions[j], the max win is
        j - i + 1 + dp[i - 1], where prizePositions[j] - prizePositions[i] == k

        O(N), 748 ms, faster than 61.44%
        """
        res = - 1
        N = len(prizePositions)
        dp = [0] * (N + 1)
        i = 1
        for j in range(1, N + 1):
            while prizePositions[j - 1] - prizePositions[i - 1] > k:
                i += 1
            dp[j] = max(dp[j - 1], j - i + 1)
            # use the current segment and the max segment previously that does
            # not overlap with us
            res = max(res, j - i + 1 + dp[i - 1])
        return res

        

sol = Solution2()
tests = [
    ([1,1,2,2,3,3,5], 2, 7),
    ([1,2,3,4], 0, 2),
    ([1,1,2,2,3,3,4,4,4,5,5,5,6,6,6,7,7,8,8], 2, 15),
]

for i, (prizePositions, k, ans) in enumerate(tests):
    res = sol.maximizeWin(prizePositions, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
