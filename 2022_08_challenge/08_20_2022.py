# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache
import heapq


class Solution0:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        """TLE
        """
        stations = [[0, startFuel]] + stations + [[target, 0]]
        N = len(stations)

        @lru_cache(maxsize=None)
        def dp(idx: int, rem_fuel: int) -> int:
            print(idx, rem_fuel)
            if idx == N - 1 and rem_fuel >= 0:
                return 0
            rem_fuel += stations[idx][1]
            res = math.inf
            for i in range(idx + 1, len(stations)):
                dist = stations[i][0] - stations[idx][0]
                if dist > rem_fuel:
                    break
                res = min(res, dp(i, rem_fuel - dist))
            return res + 1

        res = dp(0, 0)
        return res - 1 if res < math.inf else -1


class Solution1:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        """TLE"""
        stations = [[0, startFuel]] + stations
        self.res = math.inf

        def dp(idx: int, rem_fuel: int, steps: int) -> None:
            rem_fuel += stations[idx][1]
            if steps >= self.res:
                return
            if idx == len(stations) - 1 and (target - stations[idx][0]) > rem_fuel:
                return
            if (target - stations[idx][0]) <= rem_fuel:
                self.res = steps
                return
            heap = []
            for i in range(idx + 1, len(stations)):
                if rem_fuel < stations[i][0] - stations[idx][0]:
                    break
                reach = rem_fuel - (stations[i][0] - stations[idx][0]) + stations[i][1] + stations[i][0]
                heapq.heappush(heap, (-reach, i))
            while heap:
                _, max_reach_i = heapq.heappop(heap)
                dp(max_reach_i, rem_fuel - (stations[max_reach_i][0] - stations[idx][0]), steps + 1)

        dp(0, 0, 0)
        return self.res if self.res < math.inf else -1


class Solution2:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        """TLE"""
        stations = [[0, startFuel]] + stations
        N = len(stations)
        dp = [0] * N
        steps = -1
        while steps < N:
            steps += 1
            tmp = [0] * N
            for j in range(steps, N):
                for i in range(steps - 1, j):
                    if dp[i] >= stations[j][0]:
                        tmp[j] = max(tmp[j], dp[i] + stations[j][1])
            if max(tmp) >= target:
                return steps
            dp = tmp
        return -1


class Solution3:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        """LeetCode 871

        Failed. Wasn't able to figure out this DP solution. The DP is to find
        the max reach at each step. So dp[i] is the max reach at ith step. Then
        we just need to find the smallest i such that dp[i] >= target.

        To build dp, we go to each station. We know that at the kth station,
        the max number of steps is k + 1. Thus, we can query the max reach at
        k, k - 1, ..., 0 steps. If at j step, we can reach the kth station,
        then we update the max reach at dp[j + 1] by finding the max reach at
        the kth station using the max reach at jth step, i.e. dp[j]. Thus
        dp[j + 1] = max(dp[j + 1], dp[j] + stations[k][1]). If we cannot reach
        the kth station at j step, we ignore it.

        Since we use a 1D dp array, the query must go from right to left.
        Otherwise, we will update a cell in dp before visiting it.

        O(N^2), 1243 ms, faster than 19.10% 
        """
        dp = [startFuel] + [0] * len(stations)
        for i, (pos, fuel) in enumerate(stations):
            for j in range(i, -1, -1):  # the jth step
                if dp[j] >= pos:  # from the jth step, we can reach the ith station
                    dp[j + 1] = max(dp[j + 1], dp[j] + fuel)
        for i in range(len(dp)):
            if dp[i] >= target:
                return i
        return -1


class Solution4:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        """This is the heap solution. We don't refuel but try to reach as far
        as possible gas station until fuel tank contains negative fuel. When
        that happens, we know the current gas station cannot be reached without
        refueling, but any of the previous gas stations can be reached. Thus,
        we greedily choose the gas station with the highest amount of fuel to
        refuel. This is where heap comes into play. We will keep popping the
        highest amount of fuel to add to the tank, until the tank becomes
        positive. Then we repeat the whole process, until either we reach the
        destination or cannot progress any further

        O(NlogN), 163 ms, faster than 77.57%
        """
        stations.append([target, 0])
        tank = startFuel
        heap = []
        res = cur_pos = 0
        for pos, fuel in stations:
            tank -= pos - cur_pos
            while tank < 0 and heap:
                tank -= heapq.heappop(heap)
                res += 1
            if tank < 0:  # cannot progress further
                return -1
            heapq.heappush(heap, -fuel)
            cur_pos = pos
        return res if tank >= 0 else -1


sol = Solution4()
tests = [
    (1, 1, [], 0),
    (100, 1, [[10, 100]], -1),
    (100, 10, [[10,60],[20,30],[30,30],[60,40]], 2),
    (1000000, 8663, [[31,195796],[42904,164171],[122849,139112],[172890,121724],[182747,90912],[194124,112994],[210182,101272],[257242,73097],[284733,108631],[369026,25791],[464270,14596],[470557,59420],[491647,192483],[516972,123213],[577532,184184],[596589,143624],[661564,154130],[705234,100816],[721453,122405],[727874,6021],[728786,19444],[742866,2995],[807420,87414],[922999,7675],[996060,32691]], 6),
    (1000, 299, [[13,21],[26,115],[100,47],[225,99],[299,141],[444,198],[608,190],[636,157],[647,255],[841,123]], 4),
    (1000, 299, [[14,123],[145,203],[344,26],[357,68],[390,35],[478,135],[685,108],[823,186],[934,217],[959,80]], 5),
    (1000, 36, [[7,13],[10,11],[12,31],[22,14],[32,26],[38,16],[50,8],[54,13],[75,4],[85,2],[88,35],[90,9],[96,35],[103,16],[115,33],[121,6],[123,1],[138,2],[139,34],[145,30],[149,14],[160,21],[167,14],[188,7],[196,27],[248,4],[256,35],[262,16],[264,12],[283,23],[297,15],[307,25],[311,35],[316,6],[345,30],[348,2],[354,21],[360,10],[362,28],[363,29],[367,7],[370,13],[402,6],[410,32],[447,20],[453,13],[454,27],[468,1],[470,8],[471,11],[474,34],[486,13],[490,16],[495,10],[527,9],[533,14],[553,36],[554,23],[605,5],[630,17],[635,30],[640,31],[646,9],[647,12],[659,5],[664,34],[667,35],[676,6],[690,19],[709,10],[721,28],[734,2],[742,6],[772,22],[777,32],[778,36],[794,7],[812,24],[813,33],[815,14],[816,21],[824,17],[826,3],[838,14],[840,8],[853,29],[863,18],[867,1],[881,27],[886,27],[894,26],[917,3],[953,6],[956,3],[957,28],[962,33],[967,35],[972,34],[984,8],[987,12]], 32),
]

for i, (target, startFuel, stations, ans) in enumerate(tests):
    res = sol.minRefuelStops(target, startFuel, stations)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
