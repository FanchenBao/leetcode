# from pudb import set_trace; set_trace()
from typing import List
from itertools import accumulate
from bisect import bisect_right
from random import random


class Solution:
    """Produce a cumulative density function for each index by finding the
    prefix sum and divide it by the total sum. Then we can randomly produce a
    value between 0 and 1, and binary search it in the CDF array. The range
    where the random value lands is the index selected.

    O(N) for initialization, and O(logN) for pick.

    185 ms, 97% ranking.
    """

    def __init__(self, w: List[int]):
        s = sum(w)
        self.presum = [0] + [p / s for p in accumulate(w)]

    def pickIndex(self) -> int:
        return bisect_right(self.presum, random()) - 1


# sol = Solution()
# tests = [
#     ([4,2,1,3], [[1,2],[2,3],[3,4]]),
#     ([1,3,6,10,15], [[1,3]]),
#     ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
# ]

# for i, (arr, ans) in enumerate(tests):
#     res = sol.minimumAbsDifference(arr)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
