# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def countOrders(self, n: int) -> int:
        """LeetCode 1359

        Just write out n = 3 and observe how the result from n = 2 helps solve
        n = 3. Then we realize that once we know n, we can easily solve n + 1.
        Thus, this is a typical DP problem and can be solved in O(1) space.

        To be specific, given any n, there are 2 * n spaces to fill. If we
        focus on P1 and D1. If we put P1 at the first spot, D1 has 2n - 1
        different spots to take. And for each such spot, the remaining 2n - 2
        spots are the results of solving problem n - 1. And since we have
        already solved n - 1, then we immediately know that putting P1 at the
        first spot gives us (2n - 1) * f(n - 1) number of sequences. Similarly,
        we put P1 in the second spot; that gives us (2n - 2) * f(n - 1). Thus
        we have the formula:

        f(n) = (1 + 2 + ... + 2n - 1) * f(n - 1)

        This can be solved easily with DP.

        O(N), 39 ms, 75% ranking.

        UPDATE: the official solution offers two very good ways of approaching
        this problem. One is via permutation, the other probability.
        """
        pre = 1
        MOD = 10**9 + 7
        for i in range(1, n + 1):
            pre = (i * 2 * (i * 2 - 1) // 2 * pre) % MOD
        return pre
        

sol = Solution()
tests = [
    (1, 1),
    (2, 6),
    (3, 90),
    (4, 2520),
]

for i, (n, ans) in enumerate(tests):
    res = sol.countOrders(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
