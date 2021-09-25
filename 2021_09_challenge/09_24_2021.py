# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def tribonacci(self, n: int) -> int:
        """LeetCode 1137

        This is an easy question. Just follow the description of Tribonacci
        number.

        O(N), 28 ms, 83% ranking.
        """
        if n == 0:
            return 0
        if n <= 2:
            return 1
        t_0, t_1, t_2 = 0, 1, 1
        for _ in range(n - 2):
            t_0, t_1, t_2 = t_1, t_2, t_0 + t_1 + t_2
        return t_2


sol = Solution()
tests = [
    (4, 4),
    (25, 1389537),
]

for i, (n, ans) in enumerate(tests):
    res = sol.tribonacci(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
