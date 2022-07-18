# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def kInversePairs(self, n: int, k: int) -> int:
        """LeetCode 629

        Not able to do this myself. I think I solved it myself last time, but
        not today.

        The key insight is that if we know the total number of ways to form
        k inverse pairs with n numbers. Now, we want to add n + 1. If we add it
        at the end, then n + 1 number with k inverse has the same number of
        ways as n number with k inverse pairs. To put it in DP term, we can say
        dp[n + 1][k] = dp[n][k].

        Interestingly, if we shift n + 1 one position to the left. Then our
        array has one more inverse pair. This means by shiting n + 1 one
        position leftwards, we can achieve k inverse pairs in dp[n][k - 1] ways
        Pushing this logic further, we say if we shift n + 1 leftwards 2
        positions, then we can achieve k inverse pairs in dp[n][k - 2] ways.

        Thus, we say dp[n + 1][k] = dp[n][k] + dp[n][k - 1] + ... + dp[n][max(k - n, 0)]

        Another important insight is that the computation of the sum can be
        facilitated tremendously via prefix sum.

        O(NK), 760 ms, faster than 56.25%
        """
        pre = [0] * (k + 1)
        pre[0] = 1
        MOD = 10**9 + 7
        for i in range(1, n + 1):
            # iterate through n.
            cur = [0] * (k + 1)
            cur[0] = 1
            for j in range(1, k + 1):  # iterate through k
                if j > (i - 1) * i // 2:  # max number of pairs give i number of nums
                    cur[j] = cur[j - 1]
                else:
                    # build the prefix sum for the current n. Note that when
                    # shift, the most we can shift leftwards is i - 1 positions
                    # which is the length of the previous array
                    cur[j] = (cur[j - 1] + pre[j] - (0 if j <= i - 1 else pre[j - (i - 1) - 1])) % MOD
            pre = cur
        return (cur[0] if k == 0 else cur[k] - cur[k - 1]) % MOD


class Solution2:
    def kInversePairs(self, n: int, k: int) -> int:
        """This is my original solution in June 2020, but with much better
        explanation

        Here, the representation is different. pre[k] is not a cumulative sum
        but the exact number of ways to produce k inverse pairs.

        Then for cur[k - 1], we have cur[k - 1] = pre[k - 1] + pre[k - 2] + ... + pre[max(k - 1 - (n - 1), 0)]
        Interestingly, cur[k] = pre[k] + pre[k - 1] + ... + pre[max(k - (n - 1), 0)]
        This means cur[k] = cur[k - 1] + pre[k] - (pre[k - 1 - (n - 1)] if k - 1 >= n - 1 else 0)

        O(NK), 400 ms, faster than 93.75% 
        """
        pre = [0] * (k + 1)
        pre[0] = 1
        for i in range(2, n + 1):
            # iterate through n.
            cur = [0] * (k + 1)
            cur[0] = 1
            for j in range(1, k + 1):  # iterate through k
                cur[j] = cur[j - 1] + pre[j] - (pre[j - 1 - (i - 1)] if j - 1 >= i - 1 else 0)
            pre = cur
        return pre[k] % (10**9 + 7)
        

sol = Solution2()
tests = [
    (1, 0, 1),
    (2, 1, 1),
    (3, 0, 1),
    (3, 1, 2),
    (3, 2, 2),
    (3, 3, 1),
    (4, 0, 1),
    (4, 1, 3),
    (4, 2, 5),
    (5, 1, 4),
    (5, 2, 9),
    (5, 3, 15),
    (5, 9, 4),
    (1000, 1000, 663677020),
]

for i, (n, k, ans) in enumerate(tests):
    res = sol.kInversePairs(n, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
