# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        """LeetCode 1575

        After yesterday's DP, this one is not that hard to identify the state.
        dp(s, rem) reports the number of routes that go from s to finish with
        rem number of fuels. At each s, we simply go through all the locations
        reachable with rem fule, and add all the route counts together.

        O(N^2 * F), where N = len(locations) and F = fuel.
        1943 ms, faster than 77.44%
        """
        N = len(locations)
        MOD = 10**9 + 7

        @lru_cache(maxsize=None)
        def dp(s: int, rem: int) -> int:
            if rem == 0:
                if s == finish:
                    return 1
                return 0
            # if the current start is already at the finish, we record the
            # current route and search for any additional possibilities
            res = int(s == finish)
            for i in range(N):
                next_rem = rem - abs(locations[s] - locations[i])
                if i != s and next_rem >= 0:
                    res = (res + dp(i, next_rem)) % MOD
            return res

        return dp(start, fuel)


sol = Solution()
tests = [
    ([2,3,6,8,4], 1, 3, 5, 4),
    ([4,3,1], 1, 0, 6, 5),
    ([5,2,1], 0, 2, 3, 0),
]

for i, (locations, start, finish, fuel, ans) in enumerate(tests):
    res = sol.countRoutes(locations, start, finish, fuel)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
