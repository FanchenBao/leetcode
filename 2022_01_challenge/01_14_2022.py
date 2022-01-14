# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def myAtoi(self, s: str) -> int:
        """LeetCode 8

        Not difficult to program but there are quite a few edge cases that have
        surely messd me up both now and previously (more than three years ago)

        O(N), 32 ms, 86% ranking.
        """
        s = s.lstrip()
        if not s:  # edge case
            return 0
        sign, start = 1, 0
        if not s[0].isnumeric():
            if s[0] == '-':
                sign = -1
            elif s[0] != '+':
                return 0
            start += 1
        i = start
        while i < len(s) and s[i].isnumeric():
            i += 1
        if start == i:  # edge case
            return 0
        return min(max(int(s[start:i]) * sign, -(1 << 31)), (1 << 31) - 1)



sol = Solution()
tests = [
    ('42', 42),
    ('     -42', -42),
    ('4193 with words', 4193),
    ('foo 4193 with words', 0),
]

for i, (s, ans) in enumerate(tests):
    res = sol.myAtoi(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
