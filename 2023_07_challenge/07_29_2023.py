# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution1:
    def soupServings(self, n: int) -> float:
        """LeetCode 808 Fail

        This problem requires some trick. Given the range for n, I immediately
        rules out DP. But it turns that we shall examine DP values first, and
        then we will realize that at certain point, DP value becomes one when
        the amount of soup is bigger than a certain threshold. The official
        solution gives a pretty good explanation of why this is the case, but
        a simple way to think is to notice that the expected reduction in soup
        A is bigger than the expected reduction in soup B. Thus, after
        sufficient number of operations, soup A will always be empty ahead of
        soup B. In other words, then n is big enough, the answer is always 1.

        However, we don't know what that n is. So we need to use DP to find the
        actual probability when n is small. As we compute dp(a, b), we split it
        up to dp(a - 100, b), dp(a - 75, b - 25), dp(a - 50, b - 50), and
        dp(a - 25, b - 75). As long as one of them is 1, it is guaranteed that
        dp(a, b) is also 1.

        Edge case dp(0, 0) = 1/2; dp(0, non-zero) = 1; and dp(non-zero, 0) = 0

        TLE. Seems like directly handing the soup volume is not working. We
        might have to use the official solution's idea of dealing with portions
        of 25 ml.
        """
        eta = 10**(-5)  # error tolerance in online judge

        @lru_cache(maxsize=None)
        def dp(a: int, b: int) -> float:
            if a == b == 0:
                return 0.5
            if a == 0 and b != 0:
                return 1
            if a != 0 and b == 0:
                return 0
            return sum(0.25 * dp(na, nb) for na, nb in [(max(0, a - 100), b), (max(0, a - 75), max(0, b - 25)), (max(0, a - 50), max(0, b - 50)), (max(0, a - 25), max(0, b - 75))])
            
        for i in range(n):
            # once i is big enough to get to 1, no need to continue the DP
            if 1 - dp(i, i) <= eta:
                return 1
        return dp(n, n)


class Solution2:
    def soupServings(self, n: int) -> float:
        """Use portions as suggested by the official solution.

        Operation 1 has 4 portions on A and 0 portions on B.
        Operation 2 has 3 portions on A and 1 portions on B.
        Operation 3 has 2 portions on A and 2 portions on B.
        Operation 4 has 1 portions on A and 3 portions on B.

        With portions, we have much fewer states than using the soup as is.

        421 ms, faster than 9.91%
        """
        eta = 10**(-5)  # error tolerance in online judge
        max_portion = math.ceil(n / 25)

        @lru_cache(maxsize=None)
        def dp(a: int, b: int) -> float:
            if a == b == 0:
                return 0.5
            if a == 0 and b != 0:
                return 1
            if a != 0 and b == 0:
                return 0
            return sum(0.25 * dp(na, nb) for na, nb in [(max(0, a - 4), b), (max(0, a - 3), b - 1), (max(0, a - 2), max(0, b - 2)), (a - 1, max(0, b - 3))])
            
        for i in range(max_portion + 1):
            # once i is big enough to get to 1, no need to continue the DP
            if 1 - dp(i, i) <= eta:
                return 1
        return dp(max_portion, max_portion)


class Solution3:
    def soupServings(self, n: int) -> float:
        """Use portions as suggested by the official solution.

        Operation 1 has 4 portions on A and 0 portions on B.
        Operation 2 has 3 portions on A and 1 portions on B.
        Operation 3 has 2 portions on A and 2 portions on B.
        Operation 4 has 1 portions on A and 3 portions on B.
        
        Without using max, hopefully it can be a bit faster.

        324 ms, faster than 16.04%
        """
        eta = 10**(-5)  # error tolerance in online judge
        max_portion = math.ceil(n / 25)

        @lru_cache(maxsize=None)
        def dp(a: int, b: int) -> float:
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0 and b != 0:
                return 1
            if a != 0 and b <= 0:
                return 0
            return sum(0.25 * dp(na, nb) for na, nb in [(a - 4, b), (a - 3, b - 1), (a - 2, b - 2), (a - 1, b - 3)])
            
        for i in range(max_portion + 1):
            # once i is big enough to get to 1, no need to continue the DP
            if 1 - dp(i, i) <= eta:
                return 1
        return dp(max_portion, max_portion)
        

sol = Solution2()
tests = [
    (50, 0.625),
    (100, 0.71875),
]

for i, (n, ans) in enumerate(tests):
    res = sol.soupServings(n)
    if math.isclose(res, ans, abs_tol=10**(-5)):
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
