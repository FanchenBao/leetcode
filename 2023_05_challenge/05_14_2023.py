# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict, Counter
from functools import lru_cache


class Solution1:
    def maxScore(self, nums: List[int]) -> int:
        """LeetCode 1799

        A little bit trial-and-error, so not the proudest resolution of a hard
        problem. Also we changed the data structure midway from a dict to a list
        to hold all different gcds along with the indices of the nums that give
        rise to the gcd.

        The basic idea is greedy. We want the largest operation to almost always
        conincide with the largest gcd. However, to iterate through all possible
        scenarios, we have to do backtracking where at each gcd index, we can
        choose to take it or not take it.

        This will blow up run time, because it will be 2^N. However, there is an
        early termination. Since we go through gcd from large to small, once we
        hit gcd=1, there is no need to keep backtracking, because all the rest
        of the gcds will all be 1. So we can simply add up the rest of the score
        in one go.
        
        O(2^N). Worst case is none of the pairs are co-prime.
        399 ms, faster than 98.10%
        """
        gcds = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                gcds.append((math.gcd(nums[i], nums[j]), i, j))
        gcds.sort()
        self.res = 0
        used = [0] * (len(nums))

        def backtrack(op: int, idx: int, cur_score: int) -> None:
            if op == 0:
                self.res = max(self.res, cur_score)
            elif idx >= 0:
                g, i, j = gcds[idx]
                if g == 1:
                    # early termination, if the gcd is already 1, the rest of
                    # the gcd must all be one. Thus, no need to keep
                    # backtracking
                    self.res = max(self.res, (op + 1) * op // 2 + cur_score)
                    return
                if not used[i] and not used[j]:  # take the current i, j
                    used[i] = used[j] = 1
                    backtrack(op - 1, idx - 1, cur_score + op * g)
                    used[i] = used[j] = 0
                # or skip
                backtrack(op, idx - 1, cur_score)

        backtrack(len(nums) // 2, len(gcds) - 1, 0)
        return self.res


class Solution2:
    def maxScore(self, nums: List[int]) -> int:
        """Use bitmask to represent the state of the numbers that have been used
        This way, we can memoize the results of a state that have been solved
        previously. We basically go through all possible combinations to find
        the largest score.

        O(2^N * N^2 * log(A)), where N = len(nums), 2818 ms, faster than 37.98%
        """
        N = len(nums)

        @lru_cache(maxsize=None)
        def dp(state: int, op: int) -> int:
            res = 0
            for i in range(N):
                for j in range(i + 1, N):
                    to_take = (1 << i) | (1 << j)
                    if state & to_take == 0:
                        res = max(res, op * math.gcd(nums[i], nums[j]) + dp(state | to_take, op + 1))
            return res

        return dp(0, 1)


sol = Solution2()
tests = [
    ([1, 2], 1),
    ([3, 4, 6, 8], 11),
    ([1, 2, 3, 4, 5, 6], 14),
    ([5643,5643,6785,231,67,423,456,78], 22597),
    ([1,1,1,1,1,1,1,2], 10),
    ([415,230,471,705,902,87], 23),
    ([18972,164591,210610,899193,343662,850541,590706,820721,141708,355568,450092,223378,279483,707218], 848),
    ([9,17,16,15,18,13,18,20], 91),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.maxScore(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
