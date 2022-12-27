# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import deque


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        """Some medium problems are harder than this one.

        O(N), 27 ms, faster than 91.67%
        """
        res = 0
        pre = None
        for i in range(len(forts)):
            if forts[i]:
                if pre and forts[i] != pre[0]:
                    res = max(res, i - pre[1] - 1)
                pre = (forts[i], i)
        return res
        

sol = Solution()
tests = [
    ([1,0,0,-1,0,0,0,0,1], 4),
    ([0,0,1,-1], 0),
    ([1,0,0,-1], 2),
]

for i, (forts, ans) in enumerate(tests):
    res = sol.captureForts(forts)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
