# from pudb import set_trace; set_trace()
from typing import List
import math


class UndergroundSystem:

    def __init__(self):
        self.customers = {}
        self.stations = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_name, start_t = self.customers.pop(id)
        if start_name not in self.stations:
            self.stations[start_name] = {}
        if stationName not in self.stations[start_name]:
            self.stations[start_name][stationName] = [0, 0]  # [total time, number of trips]
        self.stations[start_name][stationName][0] += t - start_t
        self.stations[start_name][stationName][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, num_trips = self.stations[startStation][endStation]
        return total / num_trips  

# sol = Solution2()
# tests = [
#     ("hello", "holle"),
#     ("leetcode", "leotcede"),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
