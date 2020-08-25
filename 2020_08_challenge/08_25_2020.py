# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_right


class Solution1:
    def multi_day_cost(self, cost: int, day: int, pass_type: int) -> int:
        """Compute costs of travel using a given pass type.

        :param cost: Cost of the given pass type.
        :param day: The current day of travel to be considered.
        :parma pass_type: Must be either 7, for seven-day pass, or 30, for
            thirty-day pass.
        :return: The cost of using the given pass type.
        """
        # Get a rough estimate of the idx of the day that the pass type can 
        # still be applied to counting from the current day backwards.
        idx = bisect_right(self.days, day - pass_type + 1)
        # Make the rough estimate more precise.
        if idx > 0 and self.days[idx - 1] == day - pass_type + 1:
            idx -= 1
        return cost + self.min_costs[idx]

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """Classic DP solution.

        For each new day, consider using one-day, seven-day, and 30-day pass.
        Choose the lowest cost of them three and record it as the min cost for
        taking trip until that day. Repeat until the end.
        """
        self.min_costs = [0] * (len(days) + 1)
        self.days = days
        for i, day in enumerate(days, 1):
            self.min_costs[i] = min(
                (
                    costs[0] + self.min_costs[i - 1],  # use 1-day pass 
                    self.multi_day_cost(costs[1], day, 7),  # 7-day pass
                    self.multi_day_cost(costs[2], day, 30),  # 30-day pass
                ),
            )
        return self.min_costs[-1]


class Solution2:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """Standard solution"""
        min_costs = [0] * (days[-1] + 1)
        day_set = set(days)
        for i in range(1, days[-1] + 1):
            if i not in day_set:
                min_costs[i] = min_costs[i - 1]
            else:
                min_costs[i] = min(
                    (
                        min_costs[max(0, i - 1)] + costs[0], 
                        min_costs[max(0, i - 7)] + costs[1],
                        min_costs[max(0, i - 30)] + costs[2],
                    ),
                )
        return min_costs[-1]


sol = Solution2()
tests = [
    ([1, 4, 6, 7, 8, 20], [2, 7, 15], 11),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15], 17),
]

for i, (days, costs, ans) in enumerate(tests):
    res = sol.mincostTickets(days, costs)
    if res == ans:
        print(f'Test {i}: PASS!')
    else:
        print(f'Test {i}: FAIL. Ans: {ans}; Res: {res}')