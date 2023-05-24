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

        O(NlogN + 2^N), 3125 ms, faster than 53.96%
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


class Solution3:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        """Inspired by https://leetcode.com/problems/the-number-of-beautiful-subsets/discuss/3314361/Python-House-Robber-O(n)

        The core idea is to find subgroups of nums, such that all the values in
        the subgroup differ by k or multiples of k. Then we can always pick
        numbers from different subgroup and put them together, since they will
        never differ by k. Thus, the problem has turned into the number of ways
        to form subsets within each subgroup. Once that value is found for each
        subgroup, the result is just the multiplication of all the subgroup
        counts.

        The way to find all the numbers differ by k is via mod. All the values
        in a subgroup must have the same remainder when mod k.

        Then within each subgroup, it is a rob houses problem (i.e. we can only
        take numbers if its immediately previous k-less number is not taken)

        O(NlogN), 399 ms, faster than 61.63% 
        """
        counts = [Counter() for _ in range(k)]
        for n in nums:
            counts[n % k][n] += 1
        res = 1
        for i in range(k):  # iterate through each subgroup and find the number of subsets in the subsgroup
            # rob houses now, dp0 is the number of subsets without taking the
            # current number. dp1 is the number of subsets with the current num.
            # pre is the immediately previous number. Note that the initial
            # condition has dp0 = 1, which means we are counting empty set
            pre, dp0, dp1 = 0, 1, 0
            for n in sorted(counts[i]):
                c = 1 << counts[i][n]  # if there are multiple n, find all ways to pick n, including empty set
                if pre + k == n:  # if we take n, we cannot take pre
                    dp0, dp1 = dp0 + dp1, dp0 * (c - 1)
                else:  # we can take n and take pre
                    dp0, dp1 = dp0 + dp1, (dp0 + dp1) * (c - 1)
                pre = n
            res *= dp0 + dp1  # dp0 + dp1 is the total number of ways the current subgroup can form subsets, including empty set
        return res - 1  # not counting the situation where we have empty sets for ALL subgroup


class Solution4:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        """Optimized Solution3, also from lee215's post.

        Instead of using MOD to find the subgroups, we can simply identify
        subgroups by starting from a number, and check whether it plus k is in
        nums. We can keep checking until the next plus k is not in nums. Then
        we have the subgroup where we can apply rob houses.

        O(N), 68 ms, faster than 83.53%
        """
        count = Counter(nums)
        res = 1
        for n in count:
            if n - k not in count:  # n must be the start of a subgroup
                cur, dp0, dp1 = n, 1, 0
                while cur in count:
                    dp0, dp1 = dp0 + dp1, dp0 * ((1 << count[cur]) - 1)
                    cur += k
                res *= dp0 + dp1  # total number of subsets within the subgroup, including empty set
        return res - 1


sol = Solution4()
tests = [
    ([2,4,6], 2, 4),
    ([1], 1, 1),
    ([4,2,5,9,10,3], 1, 23),
    ([10,4,5,7,2,1], 3, 23),
    ([1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000], 1, 1048575),
    ([1,2,3,3], 1, 8),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.beautifulSubsets(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
