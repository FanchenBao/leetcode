# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def minFlipsMonoIncr(self, s: str) -> int:
        """LeetCode 926

        Set all positions to '1', record the number of flips needed. Then we go
        from left to right and set each position to '0'. If originally the value
        is '0', we reduce the number of flips, otherwise we increase. Keep track
        of the min number of flips along the way.

        O(N), 206 ms, faster than 79.49%
        """
        res = s.count('0')
        cur = res
        for num in s:
            if num == '0':
                cur -= 1
            else:
                cur += 1
            res = min(res, cur)
        return res


class Solution2:
    def minFlipsMonoIncr(self, s: str) -> int:
        """DP solution is equally good.

        Go from right to left and keep track the number of '0'. At s[i], if
        s[i] is '0', we either keep it and the min_flip is the same as the
        min_flip for s[i + 1]. Or, we flip it to '1', then the the remaining
        must all be one, which is to say the min_flip is 1 plus the number of
        remaining '0's.

        If s[i] is '1', we either keep it and the min_flip is the number of
        remaining '0's, or we flip it and the min_flip is 1 plus min_flip of
        s[i + 1]

        O(N), 231 ms, faster than 75.96%
        """
        cz = res = 0  # count of zeros
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                res = min(res, 1 + cz)
                cz += 1
            else:
                res = min(cz, 1 + res)
        return res


sol = Solution2()
tests = [
    ("00110", 1),
    ("010110", 2),
    ("00011000", 2),
    ('0', 0),
]

for i, (s, ans) in enumerate(tests):
    res = sol.minFlipsMonoIncr(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
