# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def findMinDifference(self, timePoints: List[str]) -> int:
        """It is obvious that we can sort timePoints from early to late. Once
        that is done, we can easily compute the time difference between
        consecutive time points. When performing this computation, if the
        previous minutes are larger than the current, then we need to borrow
        one hour. Also, we have to compare the last time with the first time.
        An easy to do this is to append the first time to the end of the array,
        but with 24 hours added.

        O(NlogN), 138 ms, 22% ranking.
        """
        tps = [(int(t[:2]), int(t[3:])) for t in timePoints]
        tps.sort()
        tps.append((tps[0][0] + 24, tps[0][1]))
        res = math.inf
        for i in range(1, len(tps)):
            pre_h, pre_m = tps[i - 1]
            cur_h, cur_m = tps[i]
            if cur_m < pre_m:
                cur_m += 60
                cur_h -= 1
            res = min(res, (cur_h - pre_h) * 60 + cur_m - pre_m)
        return res


class Solution2:
    def findMinDifference(self, timePoints: List[str]) -> int:
        """Convert all time point into minutes.

        Ref: https://leetcode.com/problems/minimum-time-difference/discuss/100637/Python-Straightforward-with-Explanation

        O(NlogN), 94 ms, 64% ranking.
        """
        minutes = sorted(int(t[:2]) * 60 + int(t[3:]) for t in timePoints)
        minutes.append(minutes[0] + 24 * 60)
        return min(minutes[i] - minutes[i - 1] for i in range(1, len(minutes)))


sol = Solution2()
tests = [
    (["23:59","00:00"], 1),
    (["00:00","23:59","00:00"], 0),
]

for i, (timePoints, ans) in enumerate(tests):
    res = sol.findMinDifference(timePoints)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
