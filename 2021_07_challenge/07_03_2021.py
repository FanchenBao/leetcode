# from pudb import set_trace; set_trace()
from typing import List
import math
from sortedcontainers import SortedSet
from itertools import accumulate


class Solution1:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        """TLE, brute force
        """
        m, n = len(matrix), len(matrix[0])
        prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                prefix_sum[i + 1][j + 1] = prefix_sum[i + 1][j] + val
            for j in range(n):
                prefix_sum[i + 1][j + 1] += prefix_sum[i][j + 1]

        res = -math.inf
        for i in range(m):
            for j in range(n):
                for ii in range(i + 1):
                    for jj in range(j + 1):
                        temp = prefix_sum[i + 1][j + 1] - prefix_sum[ii][j + 1] - prefix_sum[i + 1][jj] + prefix_sum[ii][jj]
                        res = max(res, temp if temp <= k else res)
                        if res == k:
                            return res
        return res


class Solution2:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        """LeetCode 363

        With the help of the solution, we are able to use SortedSet() to solve
        this problem. The key is to first understand a simpler problem: how to
        find the max sum that is smaller than k in a 1D array. It can be solved
        in O(Nlog(N)) time using SortedSet and prefix sum.

        Extending to a 2D array, the trick is to consider rectangles of one row,
        two rows, three rows, etc. And for each rectangle, we reduce it to a
        1D array by adding all the columns together. Then the problem becomes
        a 1D array problem that can be solved in O(Nlog(N)) time. To acquire
        each compressed rectangles, we need O(M^2) time. Therefore, the total
        time complexity is O(M^2Nlog(N)).

        6320 ms, 8% ranking.
        """
        m, n = len(matrix), len(matrix[0])
        prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                prefix_sum[i + 1][j + 1] = prefix_sum[i + 1][j] + val
            for j in range(n):
                prefix_sum[i + 1][j + 1] += prefix_sum[i][j + 1]

        sorted_psum = SortedSet()
        res = -math.inf
        for num_rows in range(1, m + 1):
            for i in range(num_rows - 1, m):
                sorted_psum.add(0)
                for j in range(n):
                    cur_sum = prefix_sum[i + 1][j + 1] - prefix_sum[i - num_rows + 1][j + 1]
                    idx = sorted_psum.bisect_right(cur_sum - k)
                    if sorted_psum[idx - 1] == cur_sum - k:
                        return k
                    if idx < len(sorted_psum):
                        res = max(res, cur_sum - sorted_psum[idx])
                    sorted_psum.add(cur_sum)
                sorted_psum.clear()
        return res


class Solution3:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        """Add Kadane's algo
        """

        def kadane(arr: List[int]) -> int:
            res, pre = -math.inf, 0
            for a in arr:
                pre = max(a, a + pre)
                res = max(res, pre)
            return res

        m, n = len(matrix), len(matrix[0])
        prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                prefix_sum[i + 1][j + 1] = prefix_sum[i + 1][j] + val
            for j in range(n):
                prefix_sum[i + 1][j + 1] += prefix_sum[i][j + 1]

        res = -math.inf
        for num_rows in range(1, m + 1):
            for i in range(num_rows - 1, m):
                col_sums = [
                    prefix_sum[i + 1][j + 1] - prefix_sum[i - num_rows + 1][j + 1] - prefix_sum[i + 1][j] + prefix_sum[i - num_rows + 1][j] for j in range(n)
                ]
                max_sum = kadane(col_sums)
                if max_sum == k:
                    return k
                if max_sum < k:
                    res = max(res, max_sum)
                    continue
                sorted_psum = SortedSet([0])
                for cur_sum in accumulate(col_sums):
                    idx = sorted_psum.bisect_right(cur_sum - k)
                    if sorted_psum[idx - 1] == cur_sum - k:
                        return k
                    if idx < len(sorted_psum):
                        res = max(res, cur_sum - sorted_psum[idx])
                    sorted_psum.add(cur_sum)
        return res


sol = Solution3()
tests = [
    ([[1, 0, 1], [0, -2, 3]], 2, 2),
    ([[2, 2, -1]], 3, 3),
    ([[2, 2, -1]], 0, -1),
]

for i, (matrix, k, ans) in enumerate(tests):
    res = sol.maxSumSubmatrix(matrix, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
