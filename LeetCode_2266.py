# from pudb import set_trace; set_trace()
from typing import List
from collections import deque
from itertools import groupby
import math


class Solution:
    def __init__(self):
        self.MOD = 10**9 + 7

    def build_lib(self, max_len: int, max_rep: int) -> List[int]:
        lib = [0, 1, 2, 4]
        if max_len <= 3:
            return lib
        dp = deque([[0, 0, 0], [1, 0, 0], [1, 1, 0], [1, 2, 1]])
        for i in range(4, max_len + 1):
            temp = deque([((i - 1) * (i - 2) // 2) % self.MOD, i - 1, 1])
            if max_rep == 4:
                temp.appendleft((temp[i - 3] * (i - 3) // 3) % self.MOD)
            for j in range(4):
                dp[j].append(0)
            m = -max_rep - 1
            while temp[0] and m >= -i:
                temp.appendleft(0)
                for k in range(1, max_rep + 1):
                    temp[0] = (temp[0] + (dp[-k][m - 1] if 1 - m <= len(dp[-k]) else 0)) % self.MOD
                m -= 1
            # print(dp, temp)
            lib.append(sum(temp) % self.MOD)
            dp.popleft()
            dp.append(temp)
        return lib

    def countTexts(self, pressedKeys: str) -> int:
        key_len = [(int(k), len(list(g))) for k, g in groupby(pressedKeys)]
        max_len_4, max_len_3 = 0, 0
        for k, l in key_len:
            if k in {7, 9}:
                max_len_4 = max(max_len_4, l)
            else:
                max_len_3 = max(max_len_3, l)
        lib_4 = self.build_lib(max_len_4, 4)
        lib_3 = self.build_lib(max_len_3, 3)
        res = 1
        for k, l in key_len:
            if k in {7, 9}:
                res = (res * lib_4[l]) % self.MOD
            else:
                res = (res * lib_3[l]) % self.MOD
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
]

for i, (pressedKeys, ans) in enumerate(tests):
    res = sol.countTexts(pressedKeys)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
