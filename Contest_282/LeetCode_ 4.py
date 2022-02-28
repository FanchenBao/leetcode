# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
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


sol = Solution()
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
