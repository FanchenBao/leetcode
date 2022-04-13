# from pudb import set_trace; set_trace()
from typing import List
import heapq
from functools import reduce


class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(k):
            m = heapq.heappop(nums)
            heapq.heappush(nums, m + 1)
        res, MOD = 1, 1000000007
        for n in nums:
            res = (res * n) % MOD
        return res

                
sol = Solution()
tests = [
    ([0, 4], 5, 20),
    ([6, 3, 3, 2], 2, 216),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.maximumProduct(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
