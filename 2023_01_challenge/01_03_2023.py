# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        """LeetCode 944

        298 ms, faster than 54.53%
        """
        M, N = len(strs), len(strs[0])
        res = 0
        for j in range(N):
            col = [strs[i][j] for i in range(M)]
            res += int(col != sorted(col))
        return res


sol = Solution()
tests = [
    (["cba","daf","ghi"], 1),
]

for i, (strs, ans) in enumerate(tests):
    res = sol.minDeletionSize(strs)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
