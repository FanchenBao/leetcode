# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq


class Solution1:
    def maxScore(self, nums: List[int], x: int) -> int:
        """
        Create two max heap, one containing all the possible
        max values ending at each position if the current value's
        parity is even, and the other for odd.
        
        We use the max in the max heap corresponding to the current
        value's parity.
        
        O(NlogN), 1157 ms, faster than 41.60%
        """
        queues = [[], []]
        res = 0
        for n in nums:
            par = n % 2
            cur = n - (queues[par][0] if queues[par] else 0)
            res = max(res, cur)
            heapq.heappush(queues[par], -cur)
            heapq.heappush(queues[par ^ 1], -cur + x)
            # print(queues[0], queues[1])
            # print(n)
        return res


class Solution2:
    def maxScore(self, nums: List[int], x: int) -> int:
        """
        You do NOT need a heap. All we need to do is to keep track of the
        max value available on the even and odd side. That's it.

        O(N), 906 ms, faster than 72.00%
        """
        maxes = [0, 0]
        maxes[nums[0] % 2] = nums[0]
        maxes[nums[0] % 2 ^ 1] = nums[0] - x
        res = nums[0]
        for n in nums[1:]:
            par = n % 2
            cur = n + maxes[par]
            res = max(res, cur)
            maxes[par] = max(maxes[par], cur)
            maxes[par ^ 1] = max(maxes[par ^ 1], cur - x)
        return res



sol = Solution2()
tests = [
    ([8,50,65,85,8,73,55,50,29,95,5,68,52,79], 74, 470),
    ([8,50,65,85], 74, 134),
]

for i, (nums, x, ans) in enumerate(tests):
    res = sol.maxScore(nums, x)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
