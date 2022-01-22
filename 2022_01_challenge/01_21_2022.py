# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """LeetCode 134

        The idea is to produce a list of net gas usage from gas station to gas
        station. Then we use a sliding window technique to find out whether
        starting from one gas station, the longest cumulative sum that does not
        have any negative element can reach back to the starting point. The
        benefit of sliding window is that once we have computed a range, and
        it doesn't work, we can simply ditch the starting point and continue.
        If the end points catches up to the starting point, we have our result.
        Otherwise, if the starting point exhausts the entire array, we know
        that there is no solution.

        O(N), 741 ms, 22% ranking.
        """
        net_gas = [g - c for g, c in zip(gas, cost)]
        N = len(net_gas)
        sum_net, j = 0, 0
        initiate = True
        for i in range(N):
            while sum_net >= 0 and (initiate or i != j):
                sum_net += net_gas[j]
                j += 1
                if j == N:
                    j = 0
                initiate = False
            if sum_net < 0:
                sum_net -= net_gas[i]
                if i + 1 == j:
                    initiate = True
            elif j == i:
                return i
        return -1


class Solution2:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """Replicated from my submission more than a year ago.

        The idea is to find the max sum of a subarray within net_gas. This can
        be done via Kadane's algo. Once the max sum of the subarray is found,
        and the sum of net_gas is non-negative, then it is garanteed that we
        can visit all the gas stations.

        Another important point is that in Kadane's algo, we keep track of the
        max sum ending at a particular position i in net_gas. If this max sum
        becomes negative, then we can be sure that the potential starting point
        must be i + 1, because if the starting point is anywhere before i, it
        is guaranteed that we will reach a negative sum at i

        O(N), 510 ms, 49% ranking.
        """
        net_gas = [g - c for g, c in zip(gas, cost)]
        max_sum_end_at_i = -math.inf
        start = 0
        for i, ng in enumerate(net_gas):  # no need to loop around
            max_sum_end_at_i = max(max_sum_end_at_i + ng, ng)
            if max_sum_end_at_i < 0:
                start = i + 1
        return -1 if sum(net_gas) < 0 else start


sol = Solution2()
tests = [
    ([1,2,3,4,5], [3,4,5,1,2], 3),
    ([2,3,4], [3,4,3], -1),
]

for i, (gas, cost, ans) in enumerate(tests):
    res = sol.canCompleteCircuit(gas, cost)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
