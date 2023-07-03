# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution1:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        """Same brute force as Solution2, but mysteriously faster.

        O(2^M * N), 2804 ms, faster than 22.33%
        """
        net_gain = defaultdict(int)
        self.res = 0

        def solve(idx: int, num_achiev: int) -> None:
            # print(idx, num_achiev, net_gain)
            if all(net_gain[i] == 0 for i in range(n)):
                self.res = max(self.res, num_achiev)
            if idx < len(requests):
                # grant the current request
                f, t = requests[idx]
                net_gain[f] -= 1
                net_gain[t] += 1
                solve(idx + 1, num_achiev + 1)
                net_gain[f] += 1
                net_gain[t] -= 1
                # do NOT grant the current request
                solve(idx + 1, num_achiev)

        solve(0, 0)
        return self.res


class Solution2:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        """LeetCode 1601

        Very slow, brute force, bit manipulation.

        O(2^M * N), 7251 ms, faster than 6.79%
        """
        res = 0
        M = len(requests)
        for state in range(1 << M):
            net_gain = defaultdict(int)
            cnt = 0
            for j in range(M):
                if (1 << j) & state:
                    f, t = requests[j]
                    net_gain[f] -= 1
                    net_gain[t] += 1
                    cnt += 1
            if all(net_gain[i] == 0 for i in range(n)):
                res = max(res, cnt)
        return res


class Solution3:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        """We can end early if the remaining requests cannot produce even more
        achievables.

        With this simple optimization, we speed up even more.
        1068 ms, faster than 70.87%
        """
        net_gain = defaultdict(int)
        M = len(requests)
        self.res = 0

        def solve(idx: int, num_achiev: int) -> None:
            if M - idx <= self.res - num_achiev:  # cannot produce more achievables
                return
            if all(net_gain[i] == 0 for i in range(n)):
                self.res = max(self.res, num_achiev)
            if idx < M:
                # grant the current request
                f, t = requests[idx]
                net_gain[f] -= 1
                net_gain[t] += 1
                solve(idx + 1, num_achiev + 1)
                net_gain[f] += 1
                net_gain[t] -= 1
                # do NOT grant the current request
                solve(idx + 1, num_achiev)

        solve(0, 0)
        return self.res



sol = Solution3()
tests = [
    (5, [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]], 5),
    (3, [[0,0],[1,2],[2,1]], 3),
    (4, [[0,3],[3,1],[1,2],[2,0]], 4),
    (3, [[1,2],[1,2],[2,2],[0,2],[2,1],[1,1],[1,2]], 4),
]

for i, (n, requests, ans) in enumerate(tests):
    res = sol.maximumRequests(n, requests)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
