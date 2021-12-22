# from pudb import set_trace; set_trace()
from typing import List
from collections import deque


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        """Given nums = [a1, a2, ..., an] Suppose we know F(0) = S, then F(1) = 
        F(0) - (n - 1) * an + (sum(nums) - an). This relation can be extended to
        F(k) = F(k - 1) - (n - 1)an + (sum(nums) - an)

        O(N), 1268 ms, 74% ranking.
        """
        temp = res = sum(i * n for i, n in enumerate(nums))
        S, N = sum(nums), len(nums)
        for i in range(N - 1, 0, -1):
            temp += S - N * nums[i]  # this is the trick
            res = max(res, temp)
        return res


sol = Solution()
tests = [
    ([100], 0),
    ([4,3,2,6], 26),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.maxRotateFunction(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
