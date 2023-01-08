# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """LeetCode 134

        Make a diff array and extend it once. Then sliding window to find a
        range of size len(gas) that every prefix sum is positive.

        O(N), 839 ms, faster than 60.83%
        """
        diff = [g - c for g, c in zip(gas, cost)]
        diff += diff
        cur_gas = i = 0
        for j in range(len(diff)):
            cur_gas += diff[j]
            while i <= j and cur_gas < 0:
                cur_gas -= diff[i]
                i += 1
            if j - i + 1 == len(gas):
                return i
        return -1


class Solution2:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """Use Kadane to find the max subarray sum. We can quickly determine the
        case that is impossible when the sum of diff is smaller than 0. Then
        we run Kadane, without the need to wrap around diff. Each time the max
        subarray sum ending at i is negative, it is guaranteed that the starting
        point must be beyond i, because otherwise, we will definitely end up
        negative at i. We can simply set the potential starting point at i + 1.

        O(N), 684 ms, faster than 89.22%
        """
        diff = [g - c for g, c in zip(gas, cost)]
        if sum(diff) < 0:
            return -1
        cur_max = -math.inf
        start = 0
        for i, d in enumerate(diff):
            cur_max = max(cur_max + d, d)
            if cur_max < 0:
                start = i + 1
        return start



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
