from typing import List, Dict

"""
07/14/2019

I completely failed to solve this problem, but after reading the discussion,
the solution seemed to straightforward. The trick is still to keep track of
the total of sums from start to the ith position. When this sum is positive,
we know the max interval must be from start to i. But when this sum is
negative, we need to find the max interval involving the ith element that can
make the sum of such interval become positive. To do that, we have a simple
observation. Since total[i] = total[j] + sum(j, i) and we need to find which
smallest j can make sum(j, i) positive, all we need to do is to find the
smallest j that can make total[i] - total[j] > 0. Or in other words, the
smallest j that make total[j] smaller than total[i]. The second trick here
is to realize that such j, if it exists, must make total[j] = total[i] - 1.
This is because if this j makes total[j] < total[i] - 1, say total[j] =
total[i] - 2, then to reach total[i] - 2, before total[j] there must be another
total[k] that is total[i] - 1. Otherwise, we would never have arrived at
total[i] - 2. Then this k would be the smallest index to make total[k] smaller
than total[i]. Therefore, we must find the first occurrence of total[i] - 1.

To code the algorithm, we loop through the hours list and keep adding to the
total 1 or -1. And for each new occurrence of total, we record its index in
a dictionary. If total remains positive, we increment the interval length. If
not, we compute a new interval by subtracting the index of total[i] - 1 from
the current index, and compare this new interval with the current interval
starting from the beginning, and take the max of the two.
"""


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        total = res = 0
        sumsPos: Dict[int, int] = dict()
        for i, h in enumerate(hours):
            total += 1 if h > 8 else -1
            if total > 0:
                res = i + 1
            if total not in sumsPos:
                sumsPos[total] = i
            if total - 1 in sumsPos:
                res = max(res, i - sumsPos[total - 1])
        return res


sol = Solution()
print(sol.longestWPI([9, 9, 6, 0, 6, 9]))
