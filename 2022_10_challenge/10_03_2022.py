# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        """LeetCode 1578

        Use greedy. Since we cannot rearrange or add balloons, whenever there
        are consecutive balloons, they must be removed until only one is left.
        Any other way to achieve this can be proven more costly then simply
        removing all the consecutive balloons except for one. We want to use
        as little time as possible. So the balloon left should be the one that
        also requires the max time to remove.

        O(N), 2720 ms, faster than 25.50%
        """
        res = 0
        cur_max = cur_total = neededTime[0]
        for i in range(1, len(colors)):
            if colors[i] != colors[i - 1]:
                res += cur_total - cur_max
                cur_max = cur_total = neededTime[i]
            else:
                cur_total += neededTime[i]
                cur_max = max(cur_max, neededTime[i])
        return res + cur_total - cur_max


sol = Solution()
tests = [
    ('abaac', [1,2,3,4,5], 3),
    ('abc', [1,2,3], 0),
    ('aabaa', [1,2,3,4,1], 2),
]

for i, (colors, neededTime, ans) in enumerate(tests):
    res = sol.minCost(colors, neededTime)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
