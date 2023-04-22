# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache
from collections import defaultdict


class Solution1:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        """LeetCode 879

        It is obvious that the problem requires knapsack. However, the
        constraint is a bit too big for knapsack (constraint is 100, but 2^100
        is too big a time complexity).

        The trick is that when we hit an index and the current profit is already
        larger or equal to minProfit, we do NOT have to continue with the
        original knapsack. Instead, we need to find out the total number of ways
        for the remaining groups that can fit n. Essentially, this is a second
        and simpler knapsack problem within the overall knapsack problem.

        Also, both knapsack can be memoized.

        3812 ms, faster than 26.67%

        UPDATE: Use the trick in Solution2 to reduce the number of unnecessary
        recursion calls.

        Slightly faster: 3483 ms, faster than 35.24%
        """
        MOD = 10**9 + 7
        N = len(group)
        memo = defaultdict(int)
        

        def helper2(idx: int, cur_group: int) -> int:
            k = (idx, cur_group)
            if k not in memo:
                if idx == N:
                    memo[k] = int(cur_group <= n)
                else:
                    memo[k] = helper2(idx + 1, cur_group)
                    cur_group += group[idx]
                    if cur_group <= n:
                        memo[k] = (memo[k] + helper2(idx + 1, cur_group)) % MOD
            return memo[k]


        @lru_cache(maxsize=None)
        def helper1(idx: int, cur_group: int, cur_profit: int) -> int:
            if idx == N:
                return int(cur_profit >= minProfit)
            if cur_profit >= minProfit:
                return helper2(idx, cur_group)
            res = helper1(idx + 1, cur_group, cur_profit)
            cur_group += group[idx]
            cur_profit += profit[idx]
            if cur_group <= n:
                res = (res + helper1(idx + 1, cur_group, cur_profit)) % MOD
            return res

        return helper1(0, 0, 0)


class Solution2:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        """Three level DP, But it TLE
        """
        MOD = 10**9 + 7
        N = len(group)


        @lru_cache(maxsize=None)
        def dp(idx: int, cur_group: int, cur_profit: int) -> int:
            if idx == N:
                return int(cur_profit >= minProfit)
            res = dp(idx + 1, cur_group, cur_profit)
            cur_group += group[idx]
            cur_profit += profit[idx]
            if cur_group <= n:
                res = (res + dp(idx + 1, cur_group, cur_profit)) % MOD
            return res

        return dp(0, 0, 0)


class Solution3:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        """Official solution. Almost ideantical to Solution2, but with one
        extremely important difference.

        Notice the second recursion call, the cur_profit is passed as the min
        of cur_profit and minProfit. This is to say, if the cur_profit is
        already larger than minProfit, we don't have to create a new state.
        This way, we can decrease the total amount of state visited.

        O(MNK), 3639 ms, faster than 33.33%
        """
        MOD = 10**9 + 7
        N = len(group)


        @lru_cache(maxsize=None)
        def dp(idx: int, cur_group: int, cur_profit: int) -> int:
            if idx == N:
                return int(cur_profit >= minProfit)
            res = dp(idx + 1, cur_group, cur_profit)
            cur_group += group[idx]
            cur_profit += profit[idx]
            if cur_group <= n:
                res = (res + dp(idx + 1, cur_group, min(minProfit, cur_profit))) % MOD
            return res

        return dp(0, 0, 0)


sol = Solution3()
tests = [
    (5, 3, [2,2], [2,3], 2),
    (10, 5, [2,3,5], [6,7,8], 7),
    (95, 53, [82,7,18,34,1,3,83,56,50,34,39,38,76,92,71,2,6,74,1,82,22,73,88,98,6,71,6,26,100,75,57,88,43,16,22,89,7,9,78,97,22,87,34,81,74,56,49,94,87,71,59,6,20,66,64,37,2,42,30,87,73,16,39,87,28,9,95,78,43,59,87,78,2,93,7,22,21,59,68,67,65,63,78,20,82,35,86], [45,57,38,64,52,92,31,57,31,52,3,12,93,8,11,60,55,92,42,27,40,10,77,53,8,34,87,39,8,35,28,70,32,97,88,54,82,54,54,10,78,23,82,52,10,49,8,36,9,52,81,26,5,2,30,39,89,62,39,100,67,33,86,22,49,15,94,59,47,41,45,17,99,87,77,48,22,77,82,85,97,66,3,38,49,60,66], 9883351),
    (100, 100, [18,58,88,52,54,13,50,66,83,61,100,54,60,80,1,19,78,54,67,20,57,46,12,6,14,43,64,81,30,60,48,53,86,71,51,23,71,87,95,69,11,12,41,36,69,89,91,10,98,31,67,85,16,83,83,14,14,71,33,5,40,61,22,19,34,70,50,21,91,77,4,36,16,38,56,23,68,51,71,38,63,52,14,47,25,57,95,35,58,32,1,39,48,33,89,9,1,95,90,78], [96,77,37,98,66,44,18,37,47,9,38,82,74,12,71,31,80,64,15,45,85,52,70,53,94,90,90,14,98,22,33,39,18,22,10,46,6,19,25,50,33,15,63,93,35,0,76,44,37,68,35,80,70,66,4,88,66,93,49,19,25,90,21,59,17,40,46,79,5,41,2,37,27,92,0,53,57,91,75,0,42,100,16,97,83,75,57,61,73,21,63,97,75,95,84,14,98,47,0,13], 5570822),
]

for i, (n, minProfit, group, profit, ans) in enumerate(tests):
    res = sol.profitableSchemes(n, minProfit, group, profit)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
