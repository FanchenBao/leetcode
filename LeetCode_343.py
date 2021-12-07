# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def integerBreak(self, n: int) -> int:
        """DP solution. We record in a DP array where DP[i] is the max product
        that can be obtained by splitting i into integers, except from i = 2 or
        i = 3. This is because when i = 2 or i = 3, splitting it up results in
        smaller product value compared to not splitting up. Then for any given
        n, we split it up into pairs. For each part, we find its max product
        and multiply the max products together. After going through all the
        pairs, we choose the max product as the value for n.

        O(N^2), 33 ms, 53% ranking.
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        dp = [0, 0, 2, 3]
        for i in range(4, n + 1):
            dp.append(max(dp[j] * dp[i - j] for j in range(1, i // 2 + 1)))
        return dp[n]


class Solution2:
    def integerBreak(self, n: int) -> int:
        """Read https://leetcode.com/problems/integer-break/discuss/80721/Why-factor-2-or-3-The-math-behind-this-problem.
        to understand why the optimal way for splitting a sufficiently large
        number is to break it down to as many 3s and 2s as possible. We also
        want more 3s than 2s, thus we shall try to break a number to all 3s to
        start with.

        For n % 3 == 0, it's perfect. The max product is 3^(n // 3)
        For n % 3 == 2, it's also good, because we have all 3s and one 2. The
        max product is 3^(n // 3) * 2
        For n % 3 == 1, if we take all threes, the product will be
        3^(n // 3) * 1. We are wasting the one. Thus, we simply force a 2 out of
        n, and the product is 3^((n - 2) // 3) * 2 * 2

        O(1), 45 ms.
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        q, r = divmod(n, 3)
        return 3**(q - (r & 1)) * (1 if r == 0 else (2 if r == 2 else 4))


sol = Solution2()
tests = [
    (2, 1),
    (3, 2),
    (4, 4),
    (5, 6),
    (6, 9),
    (7, 12),
    (8, 18),
    (9, 27),
    (10, 36),
]

for i, (n, ans) in enumerate(tests):
    res = sol.integerBreak(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
