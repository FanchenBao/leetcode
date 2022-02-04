# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache
from itertools import combinations


class Solution1:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """TLE"""
        N = len(nums)
        nums.sort()
        i = 0
        while i < N and nums[i] == 0:  # the appearance of 0 causes edge case
            i += 1

        def dfs(idx: int, s: int, tgt: int) -> int:
            if idx == N:
                return 0
            if s == tgt or -s == tgt:
                return 1
            if s < tgt or -s > tgt:
                return 0
            return dfs(idx + 1, s - nums[idx], tgt - nums[idx]) + dfs(idx + 1, s - nums[idx], tgt + nums[idx])
        
        if i == N:
            return 1 << i if target == 0 else 0
        return dfs(i, sum(nums), target) * (1 << i)


class Solution2:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """TLE"""
        S, N = sum(nums), len(nums)
        nums.sort()
        i = 0
        while i < N and nums[i] == 0:  # the appearance of 0 causes edge case
            i += 1
        if i == N:
            return 1 << i if target == 0 else 0
        tgt, r = divmod(S - target, 2)
        if r or tgt > S or tgt < 0:
            return 0
        if tgt == 0:
            return 1 << i
        res = 0
        new_nums = nums[i:]
        for k in range(1, min(N + 1, N - i + 1)):
            if sum(new_nums[:k]) > tgt:
                break
            for comb in combinations(new_nums, k):
                if sum(comb) == tgt:
                    res += 1
        return res * (1 << i)


sol = Solution2()
tests = [
    ([1,1,1,1,1], 3, 5),
    ([1], 1, 1),
    ([1, 0], 1, 2),
    ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],0,524288),
    ([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0,1048576),
    ([5,19,48,39,14,5,39,32,5,46,11,30,1,20,36,15,21,6,15,2], 39, 6792),
]

for i, (nums, target, ans) in enumerate(tests):
    res = sol.findTargetSumWays(nums, target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
