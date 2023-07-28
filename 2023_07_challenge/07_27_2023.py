# from pudb import set_trace; set_trace()
from typing import List
import math
from itertools import accumulate
from bisect import bisect_left


class Solution1:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        """LeetCode 2141. Fail

        Fail mainly because I couldn't reason that as long as the remaining
        battery power is sufficient to supply the amonut of battery needed, we
        can always distribute the remaining power evenly across all the laptops.

        This even distribution can be thought of like this. Let the n highest
        battery always support the laptops. The remaining batteries can pop in
        and out at any time while the main batteries are being used. Each time
        the remaining batteries go in and out, we get extra juice. Since this
        in and out can happen any number of times and does not cost any time,
        we can always evenly distribute the remaining power.

        With this reasoning, we can easily device a binary search scheme to
        solve this problem.

        O(MlogM), 590 ms
        """
        M = len(batteries)
        batteries.sort()
        psum = list(accumulate(batteries))
        lo, hi = batteries[0], psum[-1] // n + 1
        while lo < hi:
            mid = (lo + hi) // 2
            idx = bisect_left(batteries, mid)
            # M - idx is the number of batteries can supply mid minutes without
            # having to use any help
            rem_laptop = n - (M - idx)
            # no laptop needs assistance or
            # remaining laptops can be fully assisted by the other batteries
            if rem_laptop <= 0 or psum[idx - 1] >= rem_laptop * mid:
                lo = mid + 1
            else:
                hi = mid
        return lo - 1


class Solution2:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        """This is from the official solition.

        After sorting batteries, we again assign the highest n batteries to the
        laptops.

        To allow the runtime of batteries[i] to reach batteries[i + 1], we need
        help from batteries[:i]. And the amount needed is (batteries[i + 1] -
        batteries[i]) * total number of laptops up to batteries[i]. If we can
        supply it, we do so, and then move on to reaching batteries[i + 2]. If
        we cannot supply it, we simply use up the remaining batteries.

        We never have to worry about the laptops with higher juice in battery,
        because we are gradually approaching their levels, which means whatever
        level we get eventually, those laptops with higher batteries will always
        be able to handle.

        O(MlogM), 495 ms, faster than 100.00% 
        """
        M = len(batteries)
        batteries.sort()
        extra = sum(batteries[:M - n])
        i = M - n
        while i < M - 1:
            req = (batteries[i + 1] - batteries[i]) * (i + 1 - (M - n))
            if extra < req:
                break
            extra -= req
            i += 1
        return batteries[i] + extra // (i - (M - n) + 1)



sol = Solution2()
tests = [
    (2, [3,3,3], 4),
    (2, [1,1,1,1], 2),
]

for i, (n, batteries, ans) in enumerate(tests):
    res = sol.maxRunTime(n, batteries)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
