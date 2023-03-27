# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        counter = Counter(basket1 + basket2)
        if any(v % 2 == 1 for v in counter.values()):
            return -1


sol = Solution()
tests = [
    ([4,2,2,2], [1,4,1,2], 1),
    ([2,3,4,1], [3,2,5,1], -1),
    ([4,4,4,4,3], [5,5,5,5,3], 8),
]

for i, (basket1, basket2 ans) in enumerate(tests):
    res = sol.minCost(basket1, basket2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
