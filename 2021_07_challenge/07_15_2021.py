# from pudb import set_trace; set_trace()
from typing import List
import bisect


class Solution1:
    def triangleNumber(self, nums: List[int]) -> int:
        """LeetCode 611

        Fix two values and use binary search to find where the possible third
        value is going to be.

        O(N^2logN), 2476 ms, 20% ranking.
        """
        nums.sort()
        n, res = len(nums), 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                idx = bisect.bisect_left(nums, nums[i] + nums[j], lo=j + 1)
                res += idx - j - 1
        return res


class Solution2:
    def triangleNumber(self, nums: List[int]) -> int:
        """Use a DP table to precalculate some of the key results. And then we
        don't have to use binary search when fixing two values.
        
        But this solution is slower.
        """
        nums.sort()
        n, res = len(nums), 0
        max_sum = 2 * nums[-1]
        dp = [[0] * (max_sum + 1) for _ in range(n)]
        for i in range(n - 2, -1, -1):
            for j in range(nums[i + 1] + 1, max_sum + 1):
                dp[i][j] = dp[i + 1][j] + 1
        for i1 in range(n - 2):
            for i2 in range(i1 + 1, n - 1):
                res += dp[i2][nums[i1] + nums[i2]]
        return res


class Solution3:
    def triangleNumber(self, nums: List[int]) -> int:
        """Official solution O(N^2).
        """
        nums.sort()
        n, res = len(nums), 0
        for i in range(n - 2):
            k = i + 2
            for j in range(i + 1, n - 1):
                while k < n and nums[i] + nums[j] > nums[k]:
                    k += 1
                if j < k:
                    res += k - j - 1
                else:
                    break
        return res


class Solution4:
    def triangleNumber(self, nums: List[int]) -> int:
        """The 2Sum, 3Sum solution. Reference:

        https://leetcode.com/problems/valid-triangle-number/discuss/1339248/Python-sort-%2B-2-pointers-solution-explained
        """
        nums.sort()
        n, res = len(nums), 0
        for hi in range(n - 1, 1, -1):
            lo, mid = 0, hi - 1
            while lo < mid:
                if nums[lo] + nums[mid] > nums[hi]:
                    res += mid - lo
                    mid -= 1
                else:
                    lo += 1
        return res


sol = Solution4()
tests = [
    ([2, 2, 3, 4], 3),
    ([4, 2, 3, 4], 4),
    ([1, 2], 0),
    ([0, 1, 0, 1], 0),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.triangleNumber(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
