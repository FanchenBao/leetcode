# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def minOperations(self, n: int) -> int:
        """LeetCode 1551

        This is a math solution. The intuition is to always increment on the
        smallest and decrement on the biggest value at the same time. This way
        they will meet in the middle value. We do the same with the second
        smallest and second biggest. And so on and so forth.

        The target value turns out to be n. If n is odd, then the number of
        steps is the sum of 2 + 4 + ... which has length n // 2.

        If n is even, then the number of steps is the sum of 1 + 3 + ... which
        has length n // 2 as well.

        Therefore, we can write a math solution to solve this problem.

        O(1), 32 ms, 80% ranking.
        """
        half = n // 2
        start = 2 if n % 2 else 1
        return (start + start + (half - 1) * 2) * half // 2


class Solution2:
    def minOperations(self, n: int) -> int:
        """If we expand the formula on Solution1 while considering n to be even
        or odd, we shall get result = n^2 / 4 if n is even, and (n^2 - 1) / 4 if
        n is odd.

        Further reference:
        https://leetcode.com/problems/minimum-operations-to-make-array-equal/discuss/1145077/Python-Math-oneliner-explained
        """
        return n**2 // 4


sol = Solution2()
tests = [
    (3, 2),
    (6, 9),
    (7, 12),
    (1, 0),
    (2, 1),
]

for i, (s, ans) in enumerate(tests):
    res = sol.minOperations(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
