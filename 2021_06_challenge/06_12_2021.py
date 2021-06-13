# from pudb import set_trace; set_trace()
from typing import List
import heapq


class Solution1:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        """LeetCode 871

        Naive BFS, TLE
        """
        N = len(stations)
        stations.sort()
        queue = [(-1, startFuel)]
        visited = set()
        steps = -1
        while queue:
            temp = []
            for i, curr_fuel in queue:
                rg = curr_fuel + ((stations[i][1] + stations[i][0]) if i >= 0 else 0)
                if rg >= target:
                    return steps + 1
                for j in range(i + 1, N):
                    rem_fuel = rg - stations[j][0]
                    if rg >= stations[j][0]:
                        if (j, rem_fuel) not in visited:
                            visited.add((j, rem_fuel))
                            temp.append((j, rem_fuel))
                    else:
                        break
            steps += 1
            print(len(temp))
            queue = temp
        return -1


class Solution2:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        """I wasn't able to solve it. This is from the official solution:

        https://leetcode.com/problems/minimum-number-of-refueling-stops/

        It's a DP solution. The key trick is that we find the farthest one can
        go given i number of steps. This is the dp array. The goal is to find
        the smallest i such that dp[i] >= target

        We have to iterate through all stations. For each station i, we update
        dp[t] where t ranges from 1 to i + 1. Note that we must go from dp[i + 1]
        back to dp[1], because the update logic is dp[t + 1] = max(dp[t + 1],
        dp[t] - station[i][0] + station[i][1] + station[i][0]) = max(dp[t + 1],
        dp[t] + station[i][1]). This means if we go from dp[1] to dp[i + 1],
        then stations[i] might be used more than once in computing a dp[t] value.

        O(N^2), 1088 ms, 24% ranking.
        """
        dp = [startFuel] + [0] * len(stations)
        for i, (dis, fuel) in enumerate(stations):
            # IMPORTANT: must go from back to front to avoid including the same
            # station twice
            for t in range(i, -1, -1):
                if dp[t] >= dis:
                    dp[t + 1] = max(dp[t + 1], dp[t] + fuel)
        for i, max_dis in enumerate(dp):
            if max_dis >= target:
                return i
        return -1


class Solution3:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        """Heap solution from the official solution. The logic is the same, but
        the implementation is different. This one follows exactly the logic
        described. We find the max_dis. If it is not reaching the target, we
        go through all the stations that lie within max_dis and push their fuel
        to a heap. We need to use ri to signify the right most station that has
        been added into the heap in the previous round. This makes sure that
        each station is only pushed into the heap once.

        Then we pop the station with the max fuel and update max_dis and steps.
        We repeat this procedure until target is reached or heap is empty.

        The place that I got stuck was that I thought if I have used stations[i]
        than I cannot use stations[i - 1]. However, this is not true, because
        we do not care about the order of stations while popping from the heap.
        We are just saying that to reach the current max_dis, we nede stations
        i and i - 1. Their order doesn't matter.

        The solution's implementation is also interesting, but I am too tired to
        implement it.

        O(NlogN), 116 ms, 89% ranking.
        """
        max_dis = startFuel
        steps = 0
        ri = -1  # index of the right most station that we can currently reach
        heap = [0]
        while heap:
            if max_dis >= target:
                return steps
            while ri + 1 < len(stations) and stations[ri + 1][0] <= max_dis:
                heapq.heappush(heap, -stations[ri + 1][1])
                ri += 1
            if heap:
                max_dis -= heapq.heappop(heap)
                steps += 1
        return -1


sol = Solution3()
tests = [
    (1, 1, [], 0),
    (100, 1, [[10, 100]], -1),
    (100, 10, [[10, 60], [20, 30], [60, 40]], 2),
    (1000000, 53667, [[6950, 13028], [21145, 25000], [38690, 6304], [54352, 42300], [56808, 45976], [63983, 37886], [68419, 15751], [69504, 8075], [85043, 32434], [92914, 50646], [109806, 43101], [112920, 7430], [116008, 35223], [121846, 46938], [128528, 48626], [128560, 49460], [135306, 1996], [151134, 26992], [157586, 52788], [166585, 44818], [167892, 13581], [202994, 11028], [217878, 18871], [241339, 51351], [248208, 38733], [257762, 32253], [277792, 36820], [288531, 19642], [331194, 18080], [348898, 35356], [349346, 4671], [359199, 17610], [360009, 5527], [368757, 14195], [396664, 14932], [401524, 49201], [402539, 35084], [422674, 5352], [427795, 14717], [431106, 42724], [431917, 46730], [437958, 45353], [458031, 9710], [467378, 39191], [488467, 49031], [495827, 34298], [501568, 35856], [504829, 5089], [511736, 30952], [516011, 8269], [516355, 51173], [519876, 32562], [528434, 18530], [561784, 13822], [565838, 38935], [574928, 24104], [582225, 5169], [593508, 27144], [603060, 31587], [613347, 46986], [621815, 47051], [641640, 3362], [654360, 37738], [676653, 41273], [686787, 13056], [695695, 21872], [700010, 25196], [721310, 32491], [724872, 26252], [725214, 42539], [750190, 15189], [765068, 3418], [766642, 23799], [769842, 20742], [770378, 44127], [777325, 16075], [783687, 15299], [783886, 44121], [820968, 6557], [822189, 1196], [822795, 49842], [824231, 52596], [848150, 39409], [854444, 25292], [878221, 22784], [889948, 21445], [893844, 17898], [895155, 33036], [904112, 40321], [911401, 49930], [913887, 9344], [929823, 38731], [939245, 45498], [952152, 45798], [958422, 53539], [979783, 10569], [985338, 5294], [991430, 21666], [991970, 35896], [996672, 36853]], 20),
]

for i, (target, startFuel, stations, ans) in enumerate(tests):
    res = sol.minRefuelStops(target, startFuel, stations)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
