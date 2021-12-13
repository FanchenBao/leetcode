# from pudb import set_trace; set_trace()
from typing import List
from itertools import groupby


class Solution1:
    def maxPower(self, s: str) -> int:
        """grouby solution.

        48 ms, 44% ranking.
        """
        return max(len(list(g)) for _, g in groupby(s))


class Solution2:
    def maxPower(self, s: str) -> int:
        """Counting on our own.

        O(N), 44 ms, 63% ranking.
        """
        res, count = 1, 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                res = max(res, count)
                count = 1
        return max(res, count)


sol = Solution2()
tests = [
    ("leetcode", 2),
    ("abbcccddddeeeeedcba", 5),
    ("triplepillooooow", 5),
    ("hooraaaaaaaaaaay", 11),
    ("tourist", 1),
    ("cc", 2),
]

for i, (s, ans) in enumerate(tests):
    res = sol.maxPower(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
