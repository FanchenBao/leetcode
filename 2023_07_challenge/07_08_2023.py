# from pudb import set_trace; set_trace()
from typing import List
import math
import itertools
import heapq


class Solution1:
    def putMarbles(self, weights: List[int], k: int) -> int:
        """LeetCode 2551

        To break apart weights into k bags, we need to insert k - 1 separations
        into the array. Each time a separation is inserted, the score increases
        by the sum of the consecutive pair of weights on either side of the
        separation. This means to find the max score, we need to find the max
        sum of consecutive pairs. Similarly, to find the min score, we need to
        find the min sum of consecutive pairs.

        The pairs can share element, because in the case of a0, a1, a2, if we
        put separation between a0 and a1, as well as a1 and a2, the score will
        have a1 duplicated (a0 + a1 + a1 + a2). Thus, we don't have to worry
        about a value being shared by two consecutive sums.

        O(NlogN)
        """
        if k == 1:
            return 0
        pair_sums = sorted(weights[i] + weights[i + 1] for i in range(len(weights) - 1))
        return sum(pair_sums[-(k - 1):]) - sum(pair_sums[:k - 1])


class Solution2:
    def putMarbles(self, weights: List[int], k: int) -> int:
        """Some application of built-in method
        """
        pair_sums = sorted(w1 + w2 for w1, w2 in itertools.pairwise(weights))
        return sum(heapq.nlargest(k - 1, pair_sums)) - sum(heapq.nsmallest(k - 1, pair_sums))


sol = Solution2()
tests = [
    ([1,3,5,1], 2, 4),
    ([1, 3], 2, 0),
    ([25,74,16,51,12,48,15,5], 1, 0),
]

for i, (weights, k, ans) in enumerate(tests):
    res = sol.putMarbles(weights, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
