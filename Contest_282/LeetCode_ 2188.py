# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        """TLE :-(
        """
        lapcost = [math.inf] * (numLaps + 1)
        lapcost[0] = 0
        lapcost[1] = min(f for f, _ in tires) + changeTime
        queue = [(f + changeTime + f * r, f * r, r) for f, r in tires]
        lap = 1
        while queue and lap < numLaps:
            temp = []
            lap += 1
            for presum, cur, r in queue:
                if presum <= lap * lapcost[1]:
                    temp.append((presum + cur * r, cur * r, r))
                    lapcost[lap] = min(lapcost[lap], presum)
                    for i in range(1, lap // 2 + 1):
                        lapcost[lap] = min(lapcost[lap], lapcost[i] + lapcost[lap - i])
            queue = temp
            
        for l in range(lap, numLaps + 1):
            lapcost[l] = l * lapcost[1]
            for i in range(1, l // 2 + 1):
                lapcost[l] = min(lapcost[l], lapcost[i] + lapcost[l - i])
        return lapcost[numLaps] - changeTime


class Solution2:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        """I wasn't able to solve this. I checked multiple solutions and found
        these two the most helpful.

        This post gives a good explanation of why we only have to consider no
        more than 18 consecutive laps.

        https://leetcode.com/problems/minimum-time-to-finish-the-race/discuss/1802444/C%2B%2B-Linear-time-DP-with-explanation

        This post provides a good model for DP: at least one of the tire in the
        optimal arangement has to be used for some consecutive laps not larger
        than 18. Thus, we can say dp[lap] = dp[lap - last_trip] + changeTime +
        min_no_change[last_trip]. Since dp[lap - last_trip] must be known to
        compute dp[lap] (NOTE: min_no_change has already been prepared before
        the DP process), we have to run the dp as dp[1], dp[2], ...

        I was fairly close to this solution, but I fail to capture the two most
        important concepts in this problem: 18 and the way to reason the DP.

        O(18N + 18M), where N = len(tires), M = numLaps. 7134 ms, 32% ranking.
        """
        min_no_change = [math.inf] * 18
        for f, r in tires:
            presum, cur = f, f
            for i in range(1, 18):
                min_no_change[i] = min(min_no_change[i], presum)
                cur *= r
                presum += cur
        dp = [math.inf] * (numLaps + 1)
        dp[0] = 0
        for lap in range(1, numLaps + 1):
            for last_trip in range(1, min(lap, 17) + 1):
                if lap == last_trip:  # no need to change tire
                    dp[lap] = min(dp[lap], min_no_change[last_trip])
                dp[lap] = min(dp[lap], dp[lap - last_trip] + changeTime + min_no_change[last_trip])
        return dp[numLaps]


sol = Solution2()
tests = [
    ([[2,3],[3,4]], 5, 4, 21),
    ([[1,10],[2,2],[3,4]], 6, 5, 25),
    ([[3,4],[84,2],[63,8],[72,8],[82,7],[83,6],[23,2],[77,5],[51,10],[28,2],[47,9],[8,3],[48,3],[56,3],[8,10],[66,6],[92,9],[44,6],[23,5],[5,6],[86,9],[13,10],[91,3],[2,2],[8,4],[67,8],[63,6],[52,5],[42,10],[3,9],[66,5],[35,10],[63,6],[65,6],[22,8],[40,9],[43,4],[73,9],[81,5],[32,2],[30,5],[80,9],[50,4],[35,4],[52,7],[11,5],[7,8],[68,3],[54,8],[49,8]], 90, 87, 2526),
    ([[1,2]], 1, 1, 1),
]

for i, (tires, changeTime, numLaps, ans) in enumerate(tests):
    res = sol.minimumFinishTime(tires, changeTime, numLaps)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
