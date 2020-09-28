# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """This is probably one of my BEST attempt at leetcode.

        First, it passed OJ with good runtime.
        Second, I realized the two tricks in solving this problem. One is to
        create a difference array between gas and cost. This is the easy one.
        The other is to use Kadane's algorithm to find the first stretch of
        consecutive positive local maxes that equal the size of gas. This is
        because the correct starting point must ensure that the accumulated
        sum for the subsequent steps are all positive. Kadane's algorithm helps
        here because it checks the local max of the subarray sum that ends at
        a given element. If this local max is positive, that means the current
        element is on a stretch of all positive local maxes. Since the solution
        is unique, we only need to find the first such stretch that equal to the
        length of gas, and we have found the proper starting point.
        """
        dif = [g - c for g, c in zip(gas, cost)]
        size, cur_max, consec_pos_count = len(dif), -math.inf, 0
        for i, d in enumerate(dif + dif[:-1]):
            cur_max = max(cur_max + d, d)
            consec_pos_count += 1 if cur_max >= 0 else -consec_pos_count
            if consec_pos_count == size:
                return i - size + 1
        return -1


class Solution2:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """A better use of Kadane's algo"""
        dif = [g - c for g, c in zip(gas, cost)]
        start, cur_max = 0, -math.inf
        for i, d in enumerate(dif):
            cur_max = max(cur_max + d, d)
            if cur_max < 0:  # current pos cannot be the starting pos
                start = i + 1
        return -1 if sum(dif) < 0 else start


sol = Solution2()
tests = [
    ([5, 1, 2, 3, 4], [4, 4, 1, 5, 1], 4),
    ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
    ([2, 3, 4], [3, 4, 3], -1),
]

for i, (gas, cost, ans) in enumerate(tests):
    res = sol.canCompleteCircuit(gas, cost)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
