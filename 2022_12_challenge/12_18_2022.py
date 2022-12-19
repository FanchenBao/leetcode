# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """LeetCode 739

        DP. for each temperature, check its next temperature. If it is higher,
        we are done. If not, jump to the temperature that is higher than the
        next temperature, rinse and repeat.

        Amortized O(N), 3990 ms, faster than 15.90%
        """
        N = len(temperatures)
        res = [0] * N
        for i in range(N - 2, -1, -1):
            j = i + 1
            while temperatures[i] >= temperatures[j] and res[j]:
                j += res[j]
            res[i] = (j - i) if temperatures[i] < temperatures[j] else 0
        return res


sol = Solution()
tests = [
    ([73,74,75,71,69,72,76,73], [1,1,4,2,1,1,0,0]),
    ([30,40,50,60], [1,1,1,0]),
    ([30,60,90], [1,1,0]),
]

for i, (temperatures, ans) in enumerate(tests):
    res = sol.dailyTemperatures(temperatures)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
