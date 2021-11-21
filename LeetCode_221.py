# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """First we create a 2D prefix sum. This allows us to query the sum of
        any rectangle in O(1) time.

        Then we use binary search to locate the biggest square that contains all
        ones. We start with the smallest length of the square's side, and the
        largest length. If the mid length square can be found, that means we can
        try a larger length. Otherwise, we try a smaller length.

        O(MNlog(MN)), 384 ms, 13% ranking.
        """
        # 2D prefix sum
        m, n = len(matrix), len(matrix[0])
        prefsum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefsum[i][j] = int(matrix[i - 1][j - 1]) + prefsum[i][j - 1]
        for j in range(1, n + 1):
            for i in range(1, m + 1):
                prefsum[i][j] += prefsum[i - 1][j]
        # Binary search
        if prefsum[m][n] == 0:
            return 0
        lo, hi = 1, int(math.sqrt(prefsum[m][n])) + 1
        while lo < hi:
            mid = (lo + hi) // 2
            target = mid * mid
            for i in range(mid, m + 1):
                for j in range(mid, n + 1):
                    area = prefsum[i][j] - prefsum[i][j - mid] - prefsum[i - mid][j] + prefsum[i - mid][j - mid]
                    if area == target:
                        break
                else:
                    continue
                break
            else:
                hi = mid
                continue
            lo = mid + 1
        return (lo - 1)**2


class Solution2:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """DP from the official solution

        https://leetcode.com/problems/maximal-square/solution/

        dp[i][j] represents the largest square filled with '1' that ends at i, j
        position.

        O(MN), 200 ms, 83% ranking.
        """
        m, n = len(matrix), len(matrix[0])
        dp, pre, res = [0] * (n + 1), 0, 0
        for i in range(m):
            for j in range(1, n + 1):
                temp = dp[j] if i else 0
                if matrix[i][j - 1] == '1':
                    dp[j] = min([pre, dp[j - 1], dp[j]]) + 1
                    res = max(res, dp[j])
                else:
                    dp[j] = 0
                pre = temp
        return res**2


sol = Solution2()
tests = [
    ([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]], 4),
    ([["0","1"],["1","0"]], 1),
    ([["0"]], 0),
    ([["1","1","1","1","1"],["1","1","1","1","1"],["0","0","0","0","0"],["1","1","1","1","1"],["1","1","1","1","1"]], 4),
]

for i, (matrix, ans) in enumerate(tests):
    res = sol.maximalSquare(matrix)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
