# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    dp = [-1] * 31

    def fib(self, n: int) -> int:
        """LeetCode 509

        Recursion solution. This is easy to write, but we need to use
        dpization to not solve the same problem repeatedly.

        O(N), 20 ms, 99% ranking.
        """
        if self.dp[n] < 0:
            if n <= 1:
                self.dp[n] = n
            else:
                self.dp[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.dp[n]


class Solution2:
    def fib(self, n: int) -> int:
        """Iterative.

        O(N), 28 ms.
        """
        if n <= 1:
            return n
        fibs = [0] * (n + 1)
        fibs[1] = 1
        for i in range(2, n + 1):
            fibs[i] = fibs[i - 1] + fibs[i - 2]
        return fibs[n]


sol = Solution2()
tests = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
    (10, 55),
]

for i, (n, ans) in enumerate(tests):
    res = sol.fib(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
