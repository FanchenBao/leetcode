# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def numTilings(self, n: int) -> int:
        """LeetCode 790
        
        Although the algo seems very easy, the process of getting here is quite
        complex. The idea is DP. Say we have solved the following:
        
        1: 1
        2: 2
        3: 5
        4: 11

        Now we want to solve n = 5. We can split the floor this way.
        1. 2x1 + 2x4. This set up will have 11 different tilings, because we have
        solved the 2x4 problem already.
        
        2. 2x2 + 2x3. This set up needs to use the 2x2 and 2x3 results we have
        solved. However, we cannot use all of the 2x2, because one of the 2x2
        tiling has been used in the previous set up. Thus, this set up has
        5 different tilings.
        
        3. 2x3 + 2x2. This set up requires a unique 2x3 tiling that has not been
        seen in the previous two set up. Since the previous two set up always
        start from rectangles, this unique set up must not involve rectangles.
        Using the tromino, we have two unique ways to create 2x3 without
        resorting to perfect rectangles. Thus this gives us 2x2 = 4 tilings.

        4. 2x4 + 2x1. Again, we must use a unique tiling for 2x4 that does not
        involve any rectangles that can vertically split the 2x4 into two parts.
        There are two ways to form such unique tilings using trominos. Thus,
        this gives us 2x1 = 2 tilings.

        5. 2x5 + 2x0. This, like the situation in 3 and 4, requires a unique
        tiling that does not rely on clear-cut rectangles. It happens that there
        are 2 unique tilings for this.

        In total, for n = 5, we have 11 + 5 + 2 x (2 + 1 + 1) = 24

        Two important insights. First, given any n, there are only two unique
        tilings that do not require clear-cut rectangles. Both involve trominos
        at either end of the floor. When n is even, the lay out is like this:
        
        ⎡ ⎤ or ⎣ ⎦, with k horizontal dominos on the short side and k + 1 on the
        long side.

        When n is odd, the lay out is like this:

        ⎡ ⎦ or ⎣ ⎤, with k horizontal dominos on both the top and bottom sides.

        To summarize the algorithm, let dp[i] be the number of unique tilings
        for 2xi floor, and let dp[0] = 1, we have

        dp[i + 1] = dp[i] + dp[i - 1] + 2 x (dp[i - 2] + dp[i - 3] + ... + dp[0])
            = (dp[i] + dp[i - 1] + ... + dp[0]) + (dp[i - 2] + ... + dp[0])
            = sum_n + sum_n_2

        sum_n is the sum of all dp values. sum_n is the sum of the first n - 2
        dp values. In practice, we can reduce the memory usage to O(1) by
        tracking sum_n and sum_n_2, along with cur = dp[i]

        O(N), 28 ms, 94% ranking.
        """
        if n < 3:
            return n
        MOD = 10**9 + 7
        sum_n = 4
        sum_n_2 = 1
        cur = 2
        for _ in range(3, n + 1):
            temp = (sum_n + sum_n_2) % MOD
            sum_n = (sum_n + temp) % MOD
            sum_n_2 = (sum_n - cur - temp) % MOD
            cur = temp
        return cur


class Solution2:
    def numTilings(self, n: int) -> int:
        """I like my way of thinking, so I won't bother with the explanation in
        the official solution.

        However, the official solution offers one important insight.

        dp[i + 1] = dp[i] + dp[i - 1] + 2 x (dp[i - 2] + dp[i - 3] + ... + dp[0])

        Note that dp[i] = dp[i - 1] + dp[i - 2] + 2 x (dp[i - 3] + ... + dp[0])
        So we can rearrange the formula for dp[i + 1] into this:

        dp[i + 1] = dp[i] + (dp[i - 1] + dp[i - 2] + 2 x (dp[i - 3] + ... + dp[0])) + dp[i - 2]
            = 2 * dp[i] + dp[i - 2]

        This makes the algo a bit easier to write
        """
        if n < 3:
            return n
        MOD = 10**9 + 7
        dpi, dpi_1, dpi_2 = 2, 1, 1
        for _ in range(3, n + 1):
            dpi, dpi_1, dpi_2 = (2 * dpi + dpi_2) % MOD, dpi, dpi_1
        return dpi


sol = Solution2()
tests = [
    (1, 1),
    (2, 2),
    (3, 5),
    (4, 11),
    (5, 24),
    (6, 53),
    (7, 117),
]

for i, (n, ans) in enumerate(tests):
    res = sol.numTilings(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
