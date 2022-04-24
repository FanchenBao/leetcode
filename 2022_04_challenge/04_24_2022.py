# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        """LeetCode 1396

        Keep track of the total time and number of occurrences for all pairs of
        stations mentioned. Use these two pieces of information, the average
        time can be easily computed.

        272 ms, faster than 69.80% 
        """
        self.ave = defaultdict(lambda: [0, 0])
        self.passenger = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.passenger[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_name, start_t = self.passenger.pop(id)
        k = (start_name, stationName)
        self.ave[k][0] += t - start_t
        self.ave[k][1] += 1        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        k = (startStation, endStation)
        return self.ave[k][0] / self.ave[k][1]


# sol = Solution()
# tests = [
#     ([4,2,1,3], [[1,2],[2,3],[3,4]]),
#     ([1,3,6,10,15], [[1,3]]),
#     ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
# ]

# for i, (arr, ans) in enumerate(tests):
#     res = sol.minimumAbsDifference(arr)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
