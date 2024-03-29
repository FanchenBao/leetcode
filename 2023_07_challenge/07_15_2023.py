# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict
from bisect import bisect_left


class Solution1:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        """LeetCode 1751

        It is complicated, but not unsolvable. The biggest hint is that
        len(events) * k <= 10**6. This means we can solve the problem using DP
        with events index and k as state.

        We can conceive that dp(i, j) is the max score achievable attending
        any event from events[0] to events[i] as the jth event attended on the
        day. In other words dp(i, j) is a prefix max from dp(0, j) to dp(i, j)

        To find dp(i, j), we need to find dp(m, j - 1) where any events in
        events[0] to events[m] can be attended with events[i] also attended. The
        DP part is very straightforward, but to find m, we need to use binary
        search with the starting time of events[i] as the target, and search
        through all the sorted end times.

        Thus, we first sort events by end time. Then we can do a 1D DP with the
        1D array being a prefix max. Then we use binary search to find where
        in the previuos DP round we can find the max value suitable for the
        current event.

        O(KNlogN), 1105 ms, faster than 39.26% 
        """
        events.sort(key=lambda tup: (tup[1], tup[0]))
        N = len(events)
        # dp[i] is the max value obtainable among events[0:i + 1]
        dp = [events[0][2]]
        for i in range(1, N):
            dp.append(max(dp[-1], events[i][2]))
        res = dp[-1]
        for j in range(1, k):
            tmp = [0] * N
            for i in range(j, N):
                s, e, v = events[i]
                idx = bisect_left(events, s, key=lambda tup: tup[1])
                if idx > 0:
                    tmp[i] = max(tmp[i - 1], dp[idx - 1] + v)
                else:
                    tmp[i] = tmp[i - 1]
            dp = tmp
            res = max(res, dp[-1])
        return res


class Solution2:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        """We don't have to do the binary search k times. We can do all the
        binary search once, memoize it, and use it later.

        O(N(K + logN)), 952 ms, faster than 65.19%
        """
        N = len(events)
        events.sort(key=lambda tup: (tup[1], tup[0]))
        memo_bi = [bisect_left(events, s, key=lambda tup: tup[1]) for s, _, _ in events]
        # dp[i] is the max value obtainable among events[0:i + 1]
        dp = [events[0][2]]
        for i in range(1, N):
            dp.append(max(dp[-1], events[i][2]))
        res = dp[-1]
        for j in range(1, k):
            tmp = [0] * N
            for i in range(j, N):
                s, _, v = events[i]
                idx = memo_bi[i]
                if idx > 0:
                    tmp[i] = max(tmp[i - 1], dp[idx - 1] + v)
                else:
                    tmp[i] = tmp[i - 1]
            dp = tmp
            res = max(res, dp[-1])
        return res


class Solution3:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        """Inspired by the official solution WITHOUT binary search. We use DP,
        where dp(idx, rem, pre_end) is the max value possible starting from
        events[idx] with rem number of events to take, and the previous event
        ending at pre_end. However, pre_end is NOT part of the state, because if
        idx, rem have been handled already, it does not matter the exact value
        of pre_end. The sole purpose of pre_end is to check if events[idx] can
        be taken in the first place. Thus, this DP is still two-level, not
        three level.

        O(KN + NlogN), 978 ms, faster than 45.57%
        """
        memo = defaultdict(int)
        N = len(events)
        events.sort()

        def dp(idx: int, rem: int, pre_end: int) -> int:
            if idx == N or rem <= 0:
                return 0
            # This is the key to the solution! If we cannot take events[idx] due
            # to the conflict in time, we simply skip it
            if events[idx][0] <= pre_end:
                return dp(idx + 1, rem, pre_end)
            if not memo[(idx, rem)]:
                # we have two options. Take events[idx] or not take it
                memo[(idx, rem)] = max(
                    dp(idx + 1, rem, pre_end),
                    dp(idx + 1, rem - 1, events[idx][1]) + events[idx][2],
                )
            return memo[(idx, rem)]

        return dp(0, k, 0)


sol = Solution3()
tests = [
    ([[1,2,4],[3,4,3],[2,3,1]], 2, 7),
    ([[1,2,4],[3,4,3],[2,3,10]], 2, 10),
    ([[1,1,1],[2,2,2],[3,3,3],[4,4,4]], 3, 9),
    ([[87,95,42],[3,42,37],[20,42,100],[53,84,80],[10,88,38],[25,80,57],[18,38,33]], 3, 222),
]

for i, (events, k, ans) in enumerate(tests):
    res = sol.maxValue(events, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
