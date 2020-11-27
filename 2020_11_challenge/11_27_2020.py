# from pudb import set_trace; set_trace()
from typing import List
import functools


class Solution1:
    def canPartition(self, nums: List[int]) -> bool:
        """TLE. I thought backtrack is the way to go"""
        sum_nums = sum(nums)
        if sum_nums % 2:
            return False

        def backtrack(idx, target):
            if target == 0:
                return True
            for i in range(idx, len(nums)):
                if backtrack(i + 1, target - nums[i]):
                    return True
            return False

        return backtrack(0, sum_nums // 2)


class Solution2:
    def canPartition(self, nums: List[int]) -> bool:
        """TLE. In fact this solution is not much different from the previous
        one.
        """
        sum_nums = sum(nums)
        if sum_nums % 2:
            return False
        nums.sort()
        target = sum_nums // 2
        # largest num is too big for target
        if target < nums[-1]:
            return False

        def backtrack(idx, target):
            for i in range(idx, -1, -1):
                nt = target - nums[i]
                ni = i - 1
                while ni >= 0 and nt <= nums[ni]:
                    if nt == 0 or nt == nums[ni]:
                        return True
                    ni -= 1
                if backtrack(ni, nt):
                    return True
            return False

        return backtrack(len(nums) - 1, target)


class Solution3:
    def canPartition(self, nums: List[int]) -> bool:
        """lru_cache needs to be provided with more space. If not specified
        maxsize=None, this solution would TLE becasue lru_cache simply don't
        have enough room for caching.

        89% ranking
        """
        sum_nums = sum(nums)
        if sum_nums % 2:
            return False

        @functools.lru_cache(maxsize=None)
        def includes(i, target):
            if target == 0:
                return True
            if target < 0 or i == len(nums):
                return False
            return includes(i + 1, target - nums[i]) or includes(i + 1, target)

        return includes(0, sum_nums // 2)



class Solution4:
    def canPartition(self, nums: List[int]) -> bool:
        """Manual memoization. Slow as hell but passed at 6% ranking.
        """
        sum_nums = sum(nums)
        if sum_nums % 2:
            return False
        target = sum_nums // 2
        memo = [[None] * (target + 1) for _ in range(len(nums) + 1)]

        def includes(i, target):
            if target == 0:
                memo[i][target] = True
            elif target < 0 or i == len(nums):
                memo[i][target] = False
            else:
                if memo[i + 1][target] is not None:
                    res1 = memo[i + 1][target]
                else:
                    res1 = includes(i + 1, target)
                    memo[i + 1][target] = res1
                if memo[i + 1][target - nums[i]] is not None:
                    res2 = memo[i + 1][target - nums[i]]
                else:
                    res2 = includes(i + 1, target - nums[i])
                    memo[i + 1][target - nums[i]] = res2
                res = res1 or res2
                memo[i][target] = res
            return memo[i][target]

        return includes(0, target)
        

class Solution5:
    def canPartition(self, nums: List[int]) -> bool:
        """Bottom up solution. 1940 ms, 40% ranking.
        """
        sum_nums = sum(nums)
        if sum_nums % 2:
            return False
        target = sum_nums // 2
        # memo[i][j] specifies whether a subset sum of nums[0], nums[1], ... nums[i - 1] equals j
        memo = [[False] * (target + 1) for _ in range(len(nums) + 1)]
        memo[0][0] = True
        for i in range(1, len(nums) + 1):
            cur = nums[i - 1]
            for j in range(target + 1):
                if j < cur:  # cur cannot be part of j, so we extend the state of the previous row
                    memo[i][j] = memo[i - 1][j]
                else:
                    memo[i][j] = memo[i - 1][j - cur] or memo[i - 1][j]  # j either include cur, or not
        return memo[len(nums)][target]



class Solution6:
    def canPartition(self, nums: List[int]) -> bool:
        """A very smart solution. I kind of touched on this idea earlier but
        wasn't able to fulfill it.

        Also the best performance of all. 99% ranking!!
        """
        sum_nums = sum(nums)
        if sum_nums % 2:
            return False
        target = sum_nums // 2
        nums.sort(reverse=True)
        for i in range(1, len(nums)):
            temp = nums[0]  # nums[0] must be included no matter what
            for j in range(i, len(nums)):
                temp += nums[j]
                if temp > target:
                    temp -= nums[j]
                elif temp == target:
                    return True
        return nums[0] == target


sol = Solution6()
tests = [
    ([1, 5, 11, 5], True),
    ([1, 2, 3, 5], False),
    ([1], False),
    ([1, 1], True),
    ([1, 1, 5, 5, 8], True),
    ([100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 99, 97], False),
    ([23, 13, 11, 7, 6, 5, 5], True),
    ([4, 4, 4, 4, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 12, 12, 12, 12, 12, 12, 12, 12, 16, 16, 16, 16, 16, 16, 16, 16, 20, 20, 20, 20, 20, 20, 20, 20, 24, 24, 24, 24, 24, 24, 24, 24, 28, 28, 28, 28, 28, 28, 28, 28, 32, 32, 32, 32, 32, 32, 32, 32, 36, 36, 36, 36, 36, 36, 36, 36, 40, 40, 40, 40, 40, 40, 40, 40, 44, 44, 44, 44, 44, 44, 44, 44, 48, 48, 48, 48, 48, 48, 48, 48, 52, 52, 52, 52, 52, 52, 52, 52, 56, 56, 56, 56, 56, 56, 56, 56, 60, 60, 60, 60, 60, 60, 60, 60, 64, 64, 64, 64, 64, 64, 64, 64, 68, 68, 68, 68, 68, 68, 68, 68, 72, 72, 72, 72, 72, 72, 72, 72, 76, 76, 76, 76, 76, 76, 76, 76, 80, 80, 80, 80, 80, 80, 80, 80, 84, 84, 84, 84, 84, 84, 84, 84, 88, 88, 88, 88, 88, 88, 88, 88, 92, 92, 92, 92, 92, 92, 92, 92, 96, 96, 96, 96, 96, 96, 96, 96, 97, 99], False),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.canPartition(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
