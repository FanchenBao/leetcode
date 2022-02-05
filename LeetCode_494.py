# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache
from itertools import combinations
from collections import defaultdict


class Solution1:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """My recursion with memoization"""
        N = len(nums)
        nums.sort()
        i = 0
        while i < N and nums[i] == 0:  # the appearance of 0 causes edge case
            i += 1

        @lru_cache(maxsize=None)
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


class Solution3:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """Wow! I was stuck yesterday night (2022-02-02), got two TLE and was
        frustrated. Today (2022-02-03) I thought it over, and had a new idea.
        The basic logic is the same, we want to find the number of combinations
        of nums that can add up to (S - target) // 2. Of course, before we can
        do this, we must clear out the edge cases, which include:

        1. The existence of 0, which must be considered separately because we
        can always add + or - to 0 and not change the outcome.
        2. IF S - target is not an even number, then it is not possible to
        create an expression to sum up to target.
        3. If (S - target) // 2 == 0, which means all of the non-zero numbers
        must be taken to make the expression possible, then the answer with
        the non-zero elements is one.

        After the edge cases, we can create a hashmap which records the number
        of occurrences for all valid sum of any combination of numbers. We go
        from largest number to smallest, thus anytime a sum of combination
        exceeds (S - target) // 2, we don't count it. And to find the number of
        combinations that satisfies (S - target) // 2, it is the same as the
        method in 2SUM.

        76 ms, 99% ranking.
        """
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
        sum_cnt = {0: 1}
        for j in range(N - 1, i - 1, -1):
            if tgt >= nums[j]:
                res += sum_cnt.get(tgt - nums[j], 0)
                temp = sum_cnt.copy()
                for s in sum_cnt:
                    if nums[j] + s < tgt:
                        if nums[j] + s not in sum_cnt:
                            temp[nums[j] + s] = 0
                        temp[nums[j] + s] += sum_cnt[s]
                sum_cnt = temp
        return res * (1 << i)


class Solution4:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """Recursion with memo from the official solution.
        
        O(SN), where N = len(nums) and S is all possible sum values the nums
        list can take. It is at most 2000 because the sum of nums does not
        exceed 1000 (i.e. the possible sums range from -1000 to 1000)

        353 ms, 65% ranking.
        """
        N = len(nums)
        
        @lru_cache(maxsize=None)
        def helper(start: int, cur_sum: int) -> int:
            if start == N:
                return 1 if cur_sum == target else 0
            return helper(start + 1, cur_sum + nums[start]) + helper(start + 1, cur_sum - nums[start])

        return helper(0, 0)


class Solution5:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """Bottom up version of the same DP as in Solution4.
        
        O(SN), 1077 ms, 6% ranking.
        """
        N = len(nums)
        max_sum = max(abs(target), sum(nums))
        dp = [0] * (2 * max_sum + 1)
        dp[nums[0]] += 1
        dp[-nums[0]] += 1
        for n in nums[1:]:
            temp = [0] * (2 * max_sum + 1)
            for j in range(-max_sum, max_sum + 1):
                if j - n >= -max_sum:
                    temp[j] += dp[j - n]
                if j + n <= max_sum:
                    temp[j] += dp[j + n]
            dp = temp
        return dp[target]


sol = Solution5()
tests = [
    ([1], 2, 0),
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
