# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def minSteps(self, n: int) -> int:
        """We build a (N + 1)x(N + 1) 2D array. dp[i][j] is the number of steps
        to take to reach value i with j being at the copyboard. For any value
        k, we go through these pairs (k - 1, 1), (k - 2, 2), ...,
        (k // 2, k // 2). For each pair, we go to dp[k - v][v]. We know that
        by a single paste action, we can go from (k - v, v) to k. Thus, the
        steps needed to get to dp[k][v] is dp[k - v][v] + 1.

        Also, if k is even, there is another way to reach k, which is from
        (k // 2, whatever) and then do copy and paste. Thus, we need to find
        the min value of the row dp[k // 2], and then add two more steps to
        it and we get dp[k][k // 2].

        O(N^2), 2420 ms, 5% ranking.
        """
        dp = [[math.inf] * (n + 1) for _ in range(n + 1)]
        dp[1][0], dp[1][1] = 0, 1
        for i in range(2, n + 1):
            for j in range(1, i // 2 + 1):
                dp[i][j] = min(dp[i][j], dp[i - j][j] + 1)
            if i % 2 == 0:
                dp[i][i // 2] = min(dp[i][i // 2], min(dp[i // 2]) + 2)
        return min(dp[n])


class Solution2:
    def minSteps(self, n: int) -> int:
        """Official solution. It has great proof that the min steps equals to
        sum of all prime factors.

        37 ms.
        """
        res = 0
        p = 2
        while n > 1:
            while n % p == 0:
                res += p
                n //= p
            p += 1
        return res


class Solution3:
    def minSteps(self, n: int) -> int:
        """DP solution from
        https://leetcode.com/problems/2-keys-keyboard/discuss/105899/Java-DP-Solution

        BUT without the early termination of the loop. The loop can be
        terminated because of the prime factorization proof. If one already
        knows the prime factorization trick, why use DP? Thus, in my opinion,
        a real DP-based solution should not have the early termination

        O(N^2), 369 ms, 26% ranking.
        """
        dp = [math.inf] * (n + 1)
        dp[1] = 0
        for i in range(2, n + 1):
            for j in range(i // 2, 0, -1):
                if i % j == 0:
                    # Find each j that divides i. We then only need to copy
                    # and paste this j to reach i.
                    dp[i] = min(dp[i], dp[j] + i // j)
        return dp[n]


sol = Solution3()
tests = [
    (3, 3),
    (1, 0),
    (4, 4),
    (2, 2),
    (8, 6),
    (16, 8),
    (32, 10),
    (5, 5),
    (256, 16),
    (1000, 21),
]

for i, (n, ans) in enumerate(tests):
    res = sol.minSteps(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
