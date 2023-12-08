# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_left, bisect_right
from collections import Counter


class Solution1:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        """
        Sort logs, sort queries. Go from smallest query, each time binary search
        on logs to know which range to include. Then apply sliding window to
        find the count of servers that have received messages.

        O(NlogN + MlogM + NlogN), where N = len(logs), M = len(queries)
        """
        logs.sort(key=lambda tup: tup[1])
        queries_idx = sorted((q, i) for i, q in enumerate(queries))
        res = [0] * len(queries)
        # Use binary search to find the indices on logs.
        # Then use sliding window to compute the counter
        counter = Counter()
        lo, hi = 0, -1
        c = 0  # the number of servers that have received a message
        # print(logs)
        # print(queries_idx)
        for i in range(len(queries_idx)):
            rl, rr = queries_idx[i][0] - x, queries_idx[i][0]
            clo = bisect_left(logs, rl, key=lambda tup: tup[1])
            chi = bisect_right(logs, rr, key=lambda tup: tup[1]) - 1
            # print((lo, hi), (clo, chi))
            for j in range(lo, clo):
                counter[logs[j][0]] -= 1
                if (counter[logs[j][0]] == 0):
                    c -= 1
            for j in range(hi + 1, chi + 1):
                counter[logs[j][0]] += 1
                if (counter[logs[j][0]] == 1):
                    c += 1
            # print(counter)
            res[queries_idx[i][1]] = n - c
            lo, hi = clo, chi
        return res


class Solution2:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        """
        I think there is no need to do binary search at all

        O(NlogN + MlogM + N), 1566 ms, faster than 12.66%
        """
        logs.sort(key=lambda tup: tup[1])
        queries_idx = sorted((q, i) for i, q in enumerate(queries))
        res = [0] * len(queries)
        # Use binary search to find the indices on logs.
        # Then use sliding window to compute the counter
        counter = Counter()
        lo = hi = 0
        c = 0  # the number of servers that have received a message
        # print(logs)
        # print(queries_idx)
        for i in range(len(queries_idx)):
            rl, rr = queries_idx[i][0] - x, queries_idx[i][0]
            # print((lo, hi), (clo, chi))
            # Handle the lo
            j = lo
            while j < len(logs) and logs[j][1] < rl:
                counter[logs[j][0]] -= 1
                if (counter[logs[j][0]] == 0):
                    c -= 1
                j += 1
            lo = j
            # Handle the hi
            j = hi
            while j < len(logs) and logs[j][1] <= rr:
                counter[logs[j][0]] += 1
                if (counter[logs[j][0]] == 1):
                    c += 1
                j += 1
            hi = j
            # print(counter)
            res[queries_idx[i][1]] = n - c
        return res



sol = Solution2()
tests = [
    (3, [[1,3],[2,6],[1,5]], 5, [10, 11], [1, 2]),
    (4, [[2,30],[2,5],[3,9],[4,21]], 9, [11,28,16,18], [2,3,3,3]),
]

for i, (n, logs, x, queries, ans) in enumerate(tests):
    res = sol.countServers(n, logs, x, queries)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
