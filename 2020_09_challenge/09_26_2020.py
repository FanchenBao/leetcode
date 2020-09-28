# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        """OJ game me 100% ranking
    
        What I did was actively merging each interval. I checked whether the new
        interval and the previous interval overlapped. If overlap happened, we
        update the prevous interval by assigning the current end time to the
        previous interval. If there was no overlap, the previous interval time
        got added to the total and discarded. The current interval would become
        the new previous interval for the next iteration.
        """
        pre_rang = [0, 0]
        acc = 0
        for t in timeSeries:
            if t < pre_rang[1]:
                pre_rang[1] = t + duration
            else:
                acc += pre_rang[1] - pre_rang[0]
                pre_rang = [t, t + duration]
        return acc + pre_rang[1] - pre_rang[0]


class Solution2:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        """Standard solution, which is better. We only check the difference
        between consecutive times in the timeSeries. If the difference is longer
        than the duration, then the max time Ashe can be poisoned is the
        duration time. Otherwise, the poisoned time is the time difference in
        the timeSeries.
        """
        acc = 0
        for i in range(len(timeSeries) - 1):
            acc += min(timeSeries[i + 1] - timeSeries[i], duration)
        return acc + duration if timeSeries else 0


sol = Solution2()
tests = [
    ([1, 2], 2, 3),
    ([1, 4], 2, 4),
]

for i, (timeSeries, duration, ans) in enumerate(tests):
    res = sol.findPoisonedDuration(timeSeries, duration)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
