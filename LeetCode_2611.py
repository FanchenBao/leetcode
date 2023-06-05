# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        r1r2 = sorted([[r1, r2] for r1, r2 in zip(reward1, reward2)], key=lambda tup: (-tup[0], tup[1]))
        sum_1 = rem_2 = 0
        for i, (r1, r2) in enumerate(r1r2):
            if k:
                if r1 > r2:
                    sum_1 += r1
                    rem_2 += r2
                    k -= 1
            else:
                break
        else:
            for r1, r2 in sorted(r1r2, key=lambda tup: -tup[0] + tup[1]):
                if r1 <= r2:
                    if k:
                        sum_1 += r1
                        rem_2 += r2
                        k -= 1
                    else:
                        break
        return sum(reward2) - rem_2 + sum_1


sol = Solution()
tests = [
    ([1,1,3,4],[4,4,1,1], 2, 15),
    ([1,1], [1,1], 2, 2),
    ([10,10,10,10], [10,10,1,1], 2, 40),
    ([10,10,10,10], [10,10,100,100], 2, 220),
    ([1,2,2,2,3,3], [2,1,2,4,3,2], 5, 15),
]

for i, (reward1, reward2, k, ans) in enumerate(tests):
    res = sol.miceAndCheese(reward1, reward2, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
