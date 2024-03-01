# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        """
        This solution is heavily inspired by the hints

        A few key things.

        1. After performing N steps, the final result always remains the same
        regardless of the number of steps. Therefore, we only need to consider
        the first N steps.
        2. If we sort nums2 and rearrange nums1 accordingly, then given some
        j0, j1, j2, ..., jk from nums1 to remove, then the order of removal
        must follow such that nums2[j0] <= nums2[j1] <= ... <= nums2[jk]. In
        other words, it is always better to remove the bigger nums2 values
        later in the steps.
        3. We use dp in which dp[i][j] = max removal for nums1 indices 0 to j
        after i number of steps.
        """
        N = len(nums1)
        dp = [[0] * N for _ in range(N + 1)]
        s = sum(nums1)
        s2 = sum(nums2)
        sorted_nums = sorted((n2, n1) for n1, n2 in zip(nums1, nums2))
        for i in range(1, N + 1):
            s += s2
            dp[i][0] = sorted_nums[0][1] + sorted_nums[0][0] * i
            if s - dp[i][0] <= x:
                return i
            for j in range(1, N):
                # We either do not remove the jth element, or we remove it
                dp[i][j] = max(
                    dp[i][j - 1],
                    dp[i - 1][j - 1] + sorted_nums[j][1] + sorted_nums[j][0] * i,
                )
                if s - dp[i][j] <= x:
                    return i
        return -1


sol = Solution()
tests = [
    ([1, 2, 3], [1, 2, 3], 4, 3),
]

for i, (nums1, nums2, x, ans) in enumerate(tests):
    res = sol.minimumTime(nums1, nums2, x)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
