# from pudb import set_trace; set_trace()
from typing import List
from collections import deque
from itertools import groupby
import math


class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        """The dp works like this. Say we are trying to find the maximum number
        of ways to handle k number of repeated digit. Also, let's say the max
        single unit of repeat is 3. Then we know the final answer must be some
        ways start with one repeat, some start with two repeats and some three
        repeats. This means the total number of ways for k number of repeats is
        DP[k - 1] + DP[k - 2] + DP[k - 3]. Use this relation, we can compute
        the maximum number of ways for every length of repeated digits.

        O(N), 1296 ms, faster than 48.25%
        """
        MOD = 10**9 + 7
        key_len = [(int(k), len(list(g))) for k, g in groupby(pressedKeys)]
        max_len_4, max_len_3 = 0, 0
        for k, l in key_len:
            if k in {7, 9}:
                max_len_4 = max(max_len_4, l)
            else:
                max_len_3 = max(max_len_3, l)
        lib_3 = [0, 1, 2, 4, 7]
        lib_4 = [0, 1, 2, 4, 8, 15]
        for i in range(5, max_len_3 + 1):
            lib_3.append(2 * lib_3[-1] - lib_3[i - 4])
        for i in range(6, max_len_4 + 1):
            lib_4.append(2 * lib_4[-1] - lib_4[i - 5])
        res = 1
        for k, l in key_len:
            if k in {7, 9}:
                res = (res * lib_4[l]) % MOD
            else:
                res = (res * lib_3[l]) % MOD
        return res  



sol = Solution()
tests = [
    ("2", 1),
    ("22", 2),
    ("222", 4),
    ("2222", 7),
    ("22222", 13),
    ("222222", 24),
    ("2222222", 44),
    ("22233", 8),
    ("222222222222222222222222222222222222", 82876089),
    ("77777", 15),
]

for i, (pressedKeys, ans) in enumerate(tests):
    res = sol.countTexts(pressedKeys)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
