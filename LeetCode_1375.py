# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq
from itertools import accumulate


class Solution1:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        """The problem is essentially asking whether we have encountered all
        the values from 1 to step, when we are at flips[step]. We can use the
        fact that at step, if the largest value we have seen so far is step,
        then we have visited all the values from 1 to step, because all the
        values are unique. Hence, the problem can be solved by keeping track
        of the largest value encountered so far.

        O(N), 1142 ms, faster than 17.45% 
        """
        cur_max = res = 0
        for step, val in enumerate(flips, 1):
            cur_max = max(cur_max, val)
            if step == cur_max:
                res += 1
        return res


class Solution2:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        """We can use accumulate to easily obtain the largest value so far at
        each step and solve the problem in one line.

        Ref: https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/discuss/532538/JavaC%2B%2BPython-Straight-Forward-O(1)-Space

        1002 ms, faster than 23.80%
        """
        return sum(step == cur_max for step, cur_max in enumerate(accumulate(flips, max), 1))


sol = Solution2()
tests = [
    ([3,2,4,1,5], 2),
    ([4,1,2,3], 1),
]

for i, (flips, ans) in enumerate(tests):
    res = sol.numTimesAllBlue(flips)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
