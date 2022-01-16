# from pudb import set_trace; set_trace()
from typing import List
from bisect import bisect_left
from itertools import accumulate


class Solution1:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        """I wasn't able to solve this problem during the contest, but the hint
        did help point me in the right direction. The hint says use binary
        search. Thus, it is apparent that we shall set a lower bound (which
        is min(batteries)) and higher bound (which is sum(batteries) // n) for
        the answer. Then the question becomes how to evaluate whether the
        batteries can support (lo + hi) // 2 = mid number of minutes?

        If we sort batteries, then it is apparent that all the batteries with
        power more than or equal to mid can sustain mid number of minutes. So
        the question is can the remaining batteries, none of which can support
        mid number of minutes by itself, support the remaining computers? The
        answer is that as long as the remaining batteries in total can support
        the remaining computers for mid number of minutes, we are good to go.
        One way to reason with this is to assign the remaining computers to the
        highest remaining batteries. Since the left over batteries can hop in
        and out any computers, they can swap with the any battery that runs low
        to ensure that the computers don't die. Thus, as long as the remaining
        batteries are up for the task for supplying the remaining computers
        with mid number of minutes, mid is a viable solution.

        O(NlogN), 1140 ms, 40% ranking
        """
        batteries.sort()
        pref_sum = list(accumulate(batteries))
        N = len(batteries)
        lo, hi = batteries[0], sum(batteries) // n
        while lo <= hi:
            mid = (lo + hi) // 2
            idx = bisect_left(batteries, mid)
            if N - idx >= n or pref_sum[idx - 1] >= (n - (N - idx)) * mid:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo - 1


class Solution2:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        """Inspide by lee215, but essentially the same solution as above. Each
        step we check whether the max charged battery can be thrown away and
        not be considered. The criteria is if it holds more charge than the
        higher bound. If it is, then no matter what the result is, this battery
        can be used to sustain a computer.

        Each time a max-charged battery is discarded, we reduce the problem
        scope, until the max-charged battery itself cannot sustain the higher
        bound. At this point, the most number of minites that can be sustained
        is by not wasting the sum of the remaining batteries, i.e. the result
        is the sum of the remaining batteries divided by the number of the
        remaining computers

        Ref: https://leetcode.com/problems/maximum-running-time-of-n-computers/discuss/1692939/JavaC%2B%2BPython-Sort-Solution-with-Explanation-O(mlogm)
        """
        batteries.sort()
        s = sum(batteries)
        # The condition is not larger or equal to, because we want the
        # remaining batteries after the loop exists have NO WASTING. If
        # batteries[-1] == s // n, that still qualifies as no wasting.
        while batteries[-1] > s // n:
            s -= batteries.pop()
            n -= 1
        return s // n


sol = Solution2()
tests = [
    (2, [3, 3, 3], 4),
    (2, [1, 1, 1, 1], 2),
    (3, [10,10,3,5], 8),
    (1, [1], 1),
]

for i, (n, batteries, ans) in enumerate(tests):
    res = sol.maxRunTime(n, batteries)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
