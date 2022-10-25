# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import deque


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        """DP solution.

        Not too bad, but it took me a while to put it together. The DP insight
        is that we use dp[i] to represent the max sum of arr[:i + 1] after
        partitioning. For the next arr[i + 1], we count back 1, 2, 3, ... k - 1
        elements and try to form a new partition with them. We obtain the max
        value of the new partition, easily compute its sum, and use dp to
        obtain the max sum of all the previous partitions.

        The difficulty in implementation is just the arithmatic of indices.

        O(NK) time, O(K) space, 1556 ms, faster than 46.24%
        """
        dp = deque([0])
        for i in range(len(arr)):
            tmp = cur_max = j = 0
            while j < k and i - j >= 0:
                cur_max = max(cur_max, arr[i - j])
                tmp = max(tmp, cur_max * (j + 1) + dp[-j - 1])
                j += 1
            dp.append(tmp)
            if len(dp) > k + 1:
                dp.popleft()
        return dp[-1]


sol = Solution()
tests = [
    ([1], 1, 1),
    ([1,4], 2, 8),
    ([1,4,1], 3, 12),
    ([1,4,1,5], 4, 20),
    ([1,4,1,5,7], 4, 29),
    ([1,4,1,5,7,3], 4, 36),
    ([1,4,1,5,7,3,6], 4, 42),
    ([1,4,1,5,7,3,6,1], 4, 48),
    ([1,4,1,5,7,3,6,1,9], 4, 65),
    ([1,4,1,5,7,3,6,1,9,9], 4, 74),
    ([1,4,1,5,7,3,6,1,9,9,3], 4, 83),
    ([1,15,7,9,2,5,10], 3, 84),
]

for i, (arr, k, ans) in enumerate(tests):
    res = sol.maxSumAfterPartitioning(arr, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
