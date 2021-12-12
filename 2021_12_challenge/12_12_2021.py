# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter
from functools import lru_cache


class Solution1:
    def canPartition(self, nums: List[int]) -> bool:
        """LeetCode 416

        This problem is on my nightmare list. I first encountered it in
        11/27/2020, and it took many hours to crack it. I was able to solve it
        this time in half an hour. So I think this counts as improvement.

        The idea this time is that we first check the sum of nums even or odd.
        If the sum is odd, we can return False immediately. Otherwise, we obtain
        the target sum // 2.
        
        Then we find the max value in nums. If the partition is successful, then
        the max value must be included in the target. By removing the max value
        from the target, we can make the problem simpler. Thus, our new target
        is sum // 2 - max(nums).

        Then we create a counter for nums and remove one count of the max(sum).
        We then create an array from the counter, llamado `uniques`.

        Next, we perform recursion. helper(idx, tgt) returns true if it is
        possible that some combinations of uniques[idx:] including uniques[idx]
        can sum up to tgt. Thus our result is helper(i, sum // 2 - max(nums)),
        where i = 0, 1, 2, ..., len(uniques) - 1

        The helper function needs to go through all the counts for the current
        value and go through all the remaining indices in uniques.

        I don't know the time complexity. 342 ms, 83% ranking.
        """
        s = sum(nums)
        if s % 2:
            return False
        counter = Counter(nums)
        max_n = max(nums)
        target = s // 2 - max_n
        counter[max_n] -= 1
        if not counter[max_n]:
            del counter[max_n]
        uniques = list(counter.keys())
        N = len(uniques)

        @lru_cache(maxsize=None)
        def helper(idx: int, tgt: int) -> bool:
            if tgt == 0:
                return True
            if tgt < 0 or idx == N:
                return False
            cur = uniques[idx]
            for c in range(1, counter[cur] + 1):
                if any(helper(j, tgt - c * cur) for j in range(idx + 1, N + 1)):
                    return True
            return False

        return any(helper(i, target) for i in range(N))


class Solution2:
    def canPartition(self, nums: List[int]) -> bool:
        """Use knapsack problem solution.

        Ref: https://leetcode.com/problems/partition-equal-subset-sum/discuss/90592/01-knapsack-detailed-explanation

        dp[i][j] represents whether it is possible to sum up to j from any number
        combinations in nums[:i + 1]

        3760 ms, 13% ranking.
        """
        s, N = sum(nums), len(nums)
        if s % 2:
            return False
        tgt = s // 2
        dp = [[False] * (tgt + 1) for _ in range(N)]
        for i in range(N):
            dp[i][0] = True
        for j in range(1, tgt + 1):
            dp[0][j] = nums[0] == j
        for i in range(1, N):
            for j in range(1, tgt + 1):
                dp[i][j] = dp[i - 1][j]  # not taking nums[i]
                if j >= nums[i]:  # taking nums[i]
                    dp[i][j] |= dp[i - 1][j - nums[i]]
        return dp[N - 1][tgt]


class Solution3:
    def canPartition(self, nums: List[int]) -> bool:
        """Same as Solution2, but reduce space complexity
        """
        s, N = sum(nums), len(nums)
        if s % 2:
            return False
        tgt = s // 2
        dp = [nums[0] == j for j in range(tgt + 1)]
        dp[0] = True
        for i in range(1, N):
            temp = [True]
            for j in range(1, tgt + 1):
                temp.append(dp[j])  # not taking nums[i]
                if j >= nums[i]:  # taking nums[i]
                    temp[-1] |= dp[j - nums[i]]
            dp = temp
        return dp[-1]


class Solution4:
    def canPartition(self, nums: List[int]) -> bool:
        """Same as Solution3, but remove the max num.
        """
        s = sum(nums)
        if s % 2:
            return False
        nums.sort()
        tgt = s // 2 - nums.pop()
        if tgt < 0:
            return False
        dp = [nums[0] == j for j in range(tgt + 1)]
        dp[0] = True
        for i in range(1, len(nums)):
            temp = [True]
            for j in range(1, tgt + 1):
                temp.append(dp[j])  # not taking nums[i]
                if j >= nums[i]:  # taking nums[i]
                    temp[-1] |= dp[j - nums[i]]
            dp = temp
        return dp[-1]


class Solution5:
    def canPartition(self, nums: List[int]) -> bool:
        """Same as Solution3, but use one list
        """
        s = sum(nums)
        if s % 2:
            return False
        tgt = s // 2
        dp = [nums[0] == j for j in range(tgt + 1)]
        dp[0] = True
        for i in range(1, len(nums)):
            for j in range(tgt, 0, -1):  # j goes backwards
                if j >= nums[i]:  # taking nums[i]
                    dp[j] |= dp[j - nums[i]]
        return dp[-1]


sol = Solution5()
tests = [
    ([1,5,11,5], True),
    ([1,2,3,5], False),
    ([1,2,5], False),
    ([14,9,8,4,3,2], True),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.canPartition(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
