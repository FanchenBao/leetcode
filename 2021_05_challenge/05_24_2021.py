# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def toLowerCase(self, s: str) -> str:
        """LeetCode 709

        Compensation for yesterday. This is pretty easy.

        O(N), 28 ms, 73% ranking.
        """
        res = ''
        for le in s:
            res += le if not (65 <= ord(le) <= 90) else chr(ord(le) + 32)
        return res


sol = Solution()
tests = [
    ('??Hello', '??hello'),
    ('hello', 'hello'),
    ('ABC', 'abc'),
]

for i, (s, ans) in enumerate(tests):
    res = sol.toLowerCase(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
