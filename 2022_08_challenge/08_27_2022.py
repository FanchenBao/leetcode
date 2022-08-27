# from pudb import set_trace; set_trace()
from typing import List
from bisect import bisect_right, insort_right
import math
from itertools import accumulate


class Solution:
    def kadane(self, nums: List[int]) -> int:
        res, cur = -math.inf, nums[0]
        for i in range(1, len(nums)):
            cur = max(nums[i], nums[i] + cur)
            res = max(res, cur)
        return res

    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        """LeetCode 363

        I wasn't able to solve this and also didn't want to spend too much time
        on it. I checked the solution and here is the break down.

        The most important insight is how do we solve this problem in one row.
        That would be identical to a problem of finding the max subarray sum
        that is bounded by k. We know that Kadane gives us the max subarray sum
        therefore, we can do Kadane with O(N) to find the upper bound of the
        subarray sum of a row. If that is smaller than k, then we cannot
        achieve the goal.

        If Kadane gives us an upper bound larger than k, we need to analyze
        further. Since we want to find a proper subarray sum, we shall use
        prefix sum to simplify the computation of subarray sum. But we have a
        problem where prefix sum is not naturally sorted, because there are
        negative values. Therefore, we have to keep prefix sum sorted, which
        would allow us to use binary search to quickly zero in onto the largest
        subarray sum that is not larger than k. We can use SortedSet to keep
        prefix sum sorted, or we can use bisect.insort_right to insert a
        value to prefix sum and keep the prefix sum array sorted. In terms
        of implementation, we binary search current prefix sum - k. Then we
        want to use the smallest value in prefix sums that is larger than
        current prefix sum - k. If such value doesn't exist, that means we do
        not have a subarray sum satisfying the requirement.

        Now we have solved the problem in one row. To expand to multiple rows,
        we simply add all the cells in each column together, which gives us
        an array of column sums. Then we convert a multi-row problem to a
        single-row problem, except each value in the single-row is sum of all
        the cells in a column.

        The implementation below generates a column prefix sum to facilitate
        the computation of column sums later on. Then we go through all possible
        rows: 1 row, 2 rows, ...., M rows. For each num_rows, we go through
        different bottom rows, located at ii = 0, 1, 2, ...., M. Then we find
        the column sums with the bottom row at ii and height being num_rows.
        After that, we find the max subarray sum of the column sums for that
        num_rows and that ii. We go through all combinations of num_rows and ii
        to find the result.

        O(MN + M^2(N^2 + Nlog(N))), 2324 ms, faster than 88.93%
        """
        M, N = len(matrix), len(matrix[0])
        col_presum = [[0] * N for _ in range(M + 1)]
        for j in range(N):
            for i in range(1, M + 1):
                col_presum[i][j] = col_presum[i - 1][j] + matrix[i - 1][j]
        res = -math.inf
        for num_rows in range(1, M + 1):
            for ii in range(num_rows - 1, M):
                col_sums = [col_presum[ii + 1][j] - col_presum[ii - num_rows + 1][j] for j in range(N)]
                max_col_sum = self.kadane(col_sums)
                if max_col_sum == k:
                    return k
                if max_col_sum < k:
                    res = max(res, max_col_sum)
                    continue
                sorted_presum = [0]
                for pcs in accumulate(col_sums):
                    idx = bisect_right(sorted_presum, pcs - k)
                    if sorted_presum[idx - 1] == pcs - k:
                        return k
                    if idx < len(sorted_presum):
                        res = max(res, pcs - sorted_presum[idx])
                    insort_right(sorted_presum, pcs)  # insert and keep presum sorted
        return res


sol = Solution()
tests = [
    ([[1,0,1],[0,-2,3]], 2, 2),
    ([[2,2,-1]], 3, 3),
    ([[2,2,-1]], 0, -1),
]

for i, (matrix, k, ans) in enumerate(tests):
    res = sol.maxSumSubmatrix(matrix, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
