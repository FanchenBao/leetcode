# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        """LeetCode 1035

        This is exactly the same algo as longest common subsequence.

        O(MN), 182 ms, faster than 84.51%
        """
        M, N = len(nums1), len(nums2)
        dp = [0] * (N + 1)
        for i in range(M):
            tmp = [0] * (N + 1)
            for j in range(N):
                if nums1[i] == nums2[j]:
                    tmp[j + 1] = 1 + dp[j - 1 + 1]
                else:
                    tmp[j + 1] = max(dp[j + 1], tmp[j + 1 - 1])
            dp = tmp
        return dp[-1]


sol = Solution()
tests = [
    ([1,4,2], [1,2,4], 2),
    ([2,5,1,2,5], [10,5,2,1,5,2], 3),
    ([1,3,7,1,7,5], [1,9,2,5,1], 2),
]

for i, (nums1, nums2, ans) in enumerate(tests):
    res = sol.maxUncrossedLines(nums1, nums2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
