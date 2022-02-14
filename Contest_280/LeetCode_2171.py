# from pudb import set_trace; set_trace()
from typing import List
from itertools import accumulate
import math


class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        presum = list(accumulate(beans))
        N = len(beans)
        res = presum[-1] - presum[0] - beans[0] * (N - 1)
        for i in range(1, N):
            res = min(
                res,
                presum[-1] - presum[i] - beans[i] * (N - i - 1) + presum[i - 1],
            )
        return res


sol = Solution()
tests = [
    ([4,1,6,5], 4),
    ([2,10,3,2], 7),
    ([1], 0),
]

for i, (beans, ans) in enumerate(tests):
    res = sol.minimumRemoval(beans)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
