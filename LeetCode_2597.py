# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter, defaultdict
from functools import lru_cache


class Solution1:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        """Memory Limit Exceeded
        """
        nums.sort()
        N = len(nums)

        @lru_cache(maxsize=None)
        def helper(idx: int, state: int) -> int:
            if idx == N:
                return 0
            for i in range(idx):  # cannot choose nums[idx]
                if state & (1 << i) and nums[i] + k == nums[idx]:
                    res = 0
                    break
            else:  # can choose nums[idx]
                res = 1 + helper(idx + 1, state | (1 << idx))
            res += helper(idx + 1, state)  # situation where nums[idx] not chosen
            return res

        return helper(0, 0)


class Solution2:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        """This one took a long time.

        Since the size of nums does not exceed 20, we can iterate through ALL
        possible states of number choices. We sort nums to make the check easier
        and we also precompute the indices of each number.

        We use dp array to indicate whether a state is valid.

        For a given number, we iterate through all previous states, and for each
        state, we check whether the disallowed value has been chosen in that
        state. If the disallowed value has been chosen, we cannot build on top
        of that state. Otherwise, we can built on top, and the new state follows
        the validity of the previous state.
        
        One important trick is to set the empty state, or dp[0] = 1. This allows
        the inclusion of all the states that contain only one number. However,
        we must not include dp[0] in the final answer, because empty set is
        not allowed.

        O(NlogN * 2^N), 3125 ms, faster than 53.96%
        """ 
        nums.sort()
        N = len(nums)
        index_map = defaultdict(list)
        for i, n in enumerate(nums):
            index_map[n].append(i)
        
        dp = [0] * (1 << N)
        dp[0] = 1  # empty state always allow the current number to be chosen
        for i in range(N):
            for state in range(1 << i):
                for j in index_map[nums[i] - k]:
                    if state & (1 << j):
                        break
                else:
                    dp[state | (1 << i)] = dp[state]
        return sum(dp[1:])  # skip the empty set
        
        

sol = Solution2()
tests = [
    ([2,4,6], 2, 4),
    ([1], 1, 1),
    ([4,2,5,9,10,3], 1, 23),
    ([10,4,5,7,2,1], 3, 23),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.beautifulSubsets(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
