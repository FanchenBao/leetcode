# from pudb import set_trace; set_trace()
from typing import List
from random import randint
import math


class Solution0:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        """This solution is only used for generating test cases.
        
        O(2^N) runtime.
        """
        def recurse(i) -> int:
            if i == len(A):
                return max(A) - min(A)
            original = A[i]
            # plus K
            A[i] = original + K
            res1 = recurse(i + 1)
            A[i] = original - K
            res2 = recurse(i + 1)
            A[i] = original
            return min(res1, res2)

        return recurse(0)


class Solution1:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        """We write the numbers out in two rows, top row is plus K, bottom row
        is minus K. We call the min value on the top row `high_min` and the
        max value on the bottom row `low_max`.

        We consider each top row value, except the last one, as a potential
        max value of the new arry B. Say we have A[i] + K as our potential max
        value in B. There are two situations to consider.

        1. If A[i] + K >= low_max, then we know A[i] + K indeed can serve as
        a max for B. Then we need to find the largest min value, which can only
        be the smaller one between `high_min` and A[i + 1] - K.
        2. If A[i] + K < low_max, then we have to use `low_max` as the max for
        B. Then we need to find the largest min value, which can only be the
        smallest between `high_min` and A[i + 1] - K.

        We go through i from 0 to len(A) - 2. And finally conisder i = len(A) -
        1. In that case, our max must be A[-1] + K, and the largest min must
        be `high_min`. In other words, each value in A adds K. Thus eventually
        we make one more comparison between A[-1] - A[0].

        Updated according to the official solution. The code is essentially the
        same, but I will go with my intepretation.

        O(NlogN), 144 ms, 91% ranking.
        """
        A.sort()
        high_min, low_max = A[0] + K, A[-1] - K
        res = A[-1] - A[0]
        for i in range(len(A) - 1):
            res = min(res, max(A[i] + K, low_max) - min(A[i + 1] - K, high_min))
        return res


sol0 = Solution0()
sol = Solution1()
# tests = [
#     ([1], 0, 0),
#     ([0, 10], 2, 6),
#     ([1, 3, 6], 3, 3),
#     ([5, 10, 7, 7, 3, 4, 1, 1, 8, 3], 1, 7),
#     ([5, 10, 7, 7, 3, 4, 1, 1, 8, 3], 2, 5),
#     ([5, 10, 7, 7, 3, 4, 1, 1, 8, 3], 3, 4),
#     ([5, 10, 7, 7, 3, 4, 1, 1, 8, 3], 4, 6),
#     ([5, 10, 7, 7, 3, 4, 1, 1, 8, 3], 1000, 9),

# ]

tests = [
    ([randint(0, 10) for _ in range(10)], randint(0, 100)) for _ in range(100)
]

# for i, (A, K, ans) in enumerate(tests):
#     res = sol.smallestRangeII(A, K)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')

for i, (A, K) in enumerate(tests):
    ans = sol0.smallestRangeII(A, K)
    res = sol.smallestRangeII(A, K)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}, A: {A}, K: {K}')
