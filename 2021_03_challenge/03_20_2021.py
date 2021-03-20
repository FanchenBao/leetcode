# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class UndergroundSystem:
    """LeetCode 1396

    Very straightforward. Use two dictionaries, one for handling customers,
    the other the station to station time and number of times the trip has been
    taken. Each time a customer comes and goes, we use the customer dict to
    obtain the start and end stations and the time gap. Then we put this time
    gap information into the station to station dictionary. In the station to
    station dictionary, we use start station as the key of the first layer dict,
    and the end station as the key of the second layer. The value of the second
    layer dict is a tuple with (total, count), where "total" is the total time
    that the trip between the start and end stations has been accumulated, and
    "count" is the number of times this trip has been taken.

    To return the average travel time, we only need to compute total / count for
    any given pair of start and end stations.

    O(1) for all the functions in the class. 232 ms, 89% ranking.

    Update: read this solution (https://leetcode.com/problems/design-underground-system/discuss/1118415/Python-Dictionary-%2B-Counters-solution-explained)
    It is basically the same idea as ours, but its implementation is very clean
    and easy to reason with. Our solution is okay, but the stat2stat dict can be
    a bit convoluted to parse.
    """

    def __init__(self):
        self.customer = {}
        self.stat2stat = defaultdict(dict)

    def checkIn(self, id_: int, stationName: str, t: int) -> None:
        self.customer[id_] = (stationName, t)

    def checkOut(self, id_: int, stationName: str, t: int) -> None:
        start_stat, start_t = self.customer.pop(id_)
        total, count = self.stat2stat[start_stat].get(stationName, (0, 0))
        self.stat2stat[start_stat][stationName] = (total + t - start_t, count + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.stat2stat[startStation][endStation]
        return total / count

# sol = Solution3()
# tests = [
#     ('abab', True),
#     ('aba', False),
#     ('abcabcabcabc', True),
#     ('abcabcababcabcab', True),
#     ('abcbac', False),
#     ('aabaabaab', True),
#     ('a', False),
#     ('aaaaaaa', True),
#     ('aaaaab', False),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.repeatedSubstringPattern(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
