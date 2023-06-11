# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_right


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        """LeetCode 1802

        Use binary search. Pick a max value for nums[index], and compute the
        min sum of nums possible. The min sum is achieved by always decreasing
        the values in nums from nums[index] to both sides. If the min sum is
        still larger than maxSum, that means the current pick is not going to
        work. We need to reduce it. Otherwise, we can try increase it. The final
        pick that exits binary search is one larger than the correct solution.

        One edge case is that the starting hi has to be maxSum + 1, because it
        is possible that the answer itself is maxSum.

        O(log(maxSum)), 57 ms, faster than 29.77%
        """
        lo, hi = 1, maxSum + 1
        while lo < hi:
            mid = (lo + hi) // 2
            min_sum = 0
            min_val_index_left = index - (mid - 1)
            if min_val_index_left <= 0:
                min_sum += (mid + mid - index) * (index + 1) // 2
            else:
                min_sum += (mid + 1) * mid // 2 + min_val_index_left
            min_val_index_right = index + (mid - 1)
            if min_val_index_right >= n - 1:
                min_sum += (mid - 1 + mid - (n - 1 - index)) * (n - 1 - index) // 2
            else:
                min_sum += (mid - 1 + 1) * (mid - 1) // 2 + (n - 1 - min_val_index_right)
            if min_sum > maxSum:
                hi = mid
            else:
                lo = mid + 1
        return lo - 1


sol = Solution()
tests = [
    (4, 2, 6, 2),
    (6, 1, 10, 3),
    (1, 0, 24, 24),
]

for i, (n, index, maxSum, ans) in enumerate(tests):
    res = sol.maxValue(n, index, maxSum)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
