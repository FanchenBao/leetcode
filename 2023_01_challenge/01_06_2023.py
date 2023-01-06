# from pudb import set_trace; set_trace()
from typing import List
import math
from itertools import accumulate
from bisect import bisect_right


class Solution1:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        """LeetCode 1833

        Sort and take the smallest prefix sum that is smaller than coins

        O(NlogN), 2081 ms, faster than 32.98% 
        """
        costs.sort()
        total = i = 0
        while i < len(costs):
            total += costs[i]
            if total > coins:
                break
            i += 1
        return i


class Solution2:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        """Use binary search
        
        2259 ms, faster than 19.11%
        """
        return bisect_right(list(accumulate(sorted(costs))), coins)


sol = Solution2()
tests = [
    ([1,3,2,4,1], 7, 4),
    ([10,6,8,7,7,8], 5, 0),
    ([1,6,3,1,2,5], 20, 6),
    ([2], 2, 1),
]

for i, (costs, coins, ans) in enumerate(tests):
    res = sol.maxIceCream(costs, coins)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
