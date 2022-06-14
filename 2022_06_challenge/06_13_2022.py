# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """LeetCode 120

        Very basic DP. There are a few edge cases that need to be considered.
        For instance, the row above the current is not as long as the current,
        thus when we do triangle[i - 1][j], we must ensure that j is within the
        range of triangle[i - 1]
        """
        for i in range(1, len(triangle)):
            N = len(triangle[i])
            for j in range(N):
                triangle[i][j] += min(triangle[i - 1][j] if j < N - 1 else math.inf, triangle[i - 1][j - 1] if j > 0 else math.inf)
        return min(triangle[-1])


# sol = Solution()
# tests = [
#     ([4,2,1,3], [[1,2],[2,3],[3,4]]),
#     ([1,3,6,10,15], [[1,3]]),
#     ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
# ]

# for i, (arr, ans) in enumerate(tests):
#     res = sol.minimumAbsDifference(arr)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
