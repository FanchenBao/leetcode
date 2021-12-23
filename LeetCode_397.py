# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache


class Solution1:
    def integerReplacement(self, n: int) -> int:
        """TLE, which means O(N) is too slow.
        """
        dp = [0, 0]
        for i in range(2, n + 1):
            if i % 2:  # odd
                dp.append(min(1 + dp[i - 1], 2 + dp[(i + 1) // 2]))
            else:  # even
                dp.append(1 + dp[i // 2])
        return dp[n]


class Solution2:
    def integerReplacement(self, n: int) -> int:
        """Top down.

        This shall be faster because we do not compute every value.
        Indeed, top down avoids computation of unnecessary values. Since each
        step we reduce the value by half, the time complexity is O(logN).

        O(logN), 32 ms, 68% ranking.
        """

        @lru_cache(maxsize=None)
        def dp(num: int) -> int:
            if num == 1:
                return 0
            return min(1+ dp(num - 1), 1 + dp(num + 1)) if num % 2 else 1 + dp(num // 2)
            
        return dp(n)


sol = Solution2()
tests = [
    (1, 0),
    (2, 1),
    (3, 2),
    (4, 2),
    (5, 3),
    (6, 3),
    (7, 4),
    (8, 3),
]

for i, (n, ans) in enumerate(tests):
    res = sol.integerReplacement(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
