# from pudb import set_trace; set_trace()
from typing import List
import math
import itertools
import heapq


class Solution1:
    def putMarbles(self, weights: List[int], k: int) -> int:
        """To get k subarrays out of weights, we need to slice it k - 1 times.
        Each slice produces two neighbors, which belong to the end of the
        previous subarray and the start of the next subarray.

        Thus, the score of a partition is the sum of all neighbors after the
        slicing plus the first and last value in weights.

        Since the first and last values exist in both the max and min partition,
        they will be cancelled. Thus we just need to find the sum of all
        neighbors in the max partition and that of the min partition.

        Since the scores are only associated with the neighbors, we can find
        the sum of all neighbors, sort them, and easily obtain the sum of the
        last k - 1 elements as the max score and the sum of the first k - 1
        elements as the min score.

        One thing to pay attention to is that if we use negative indexing to
        find the last k - 1 elements, we will be bitten if k = 1.

        O(NlogN + K)
        """
        tmp = sorted(weights[i] + weights[i - 1] for i in range(1, len(weights)))
        return sum(tmp[len(tmp)-k + 1:]) - sum(tmp[:k - 1])


class Solution2:
    def putMarbles(self, weights: List[int], k: int) -> int:
        """lee215 offers a solution based on priority queue, which is faster,
        and uses some built-in functions of python. It looks like magic
        """
        tmp = [w1 + w2 for w1, w2 in itertools.pairwise(weights)]
        return sum(heapq.nlargest(k - 1, tmp)) - sum(heapq.nsmallest(k - 1, tmp))


sol = Solution2()
tests = [
    ([1,3,5,1], 2, 4),
    ([1,3], 2, 0),
    ([25,74,16,51,12,48,15,5], 1, 0),
]

for i, (weights, k, ans) in enumerate(tests):
    res = sol.putMarbles(weights, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
