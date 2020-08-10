#! /usr/bin/env python3
from typing import List

"""09/04/2019

Fairly straightforward. Use cumulative sum to compute sums of consecutive calories.
The algorithm takes O(n) time to finish. This solution clocked in at 240 ms, 77%
"""


class Solution:
    def dietPlanPerformance(
        self, calories: List[int], k: int, lower: int, upper: int
    ) -> int:
        cum_sum: List[int] = [0] * (len(calories) + 1)
        for i, cal in enumerate(calories):
            cum_sum[i + 1] = cum_sum[i] + cal
        score = 0
        for i in range(k, len(calories) + 1):
            if cum_sum[i] - cum_sum[i - k] > upper:
                score += 1
            elif cum_sum[i] - cum_sum[i - k] < lower:
                score -= 1
        return score


sol = Solution()
calories = [6, 5, 0, 0]
k = 2
lower = 1
upper = 5
print(sol.dietPlanPerformance(calories, k, lower, upper))
