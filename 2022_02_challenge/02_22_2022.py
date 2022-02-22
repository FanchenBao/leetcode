# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        """LeetCode 171

        This is as if the column title is a numbering system with base 26.

        O(N), 37 ms, 68% ranking.
        """
        return sum((ord(a) - 64) * (26**i) for i, a in enumerate(columnTitle[::-1]))


sol = Solution()
tests = [
    ('A', 1),
    ('AB', 28),
    ('ZY', 701),
]

for i, (columnTitle, ans) in enumerate(tests):
    res = sol.titleToNumber(columnTitle)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
