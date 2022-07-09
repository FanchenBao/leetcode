# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache
import heapq
import math
from collections import deque


class Solution1:
    def maxResult(self, nums: List[int], k: int) -> int:
        """TLE"""
        N = len(nums)

        @lru_cache
        def dp(idx: int) -> int:
            if idx == 0:
                return nums[0]
            return max(dp(i) + nums[idx] for i in range(idx - 1, max(idx - k, 0) - 1, -1))

        return dp(N - 1)


class Solution2:
    def maxResult(self, nums: List[int], k: int) -> int:
        """LeetCode 1696

        Use a heap to keep track of the max value in the jump range before the
        current index.

        A bit larger than O(NlogN). 2735 ms, faster than 5.04%
        """
        N = len(nums)
        cur_max = nums[0]
        max_heap = [(-nums[0], 0)]
        for i in range(1, N):
            while max_heap[0][1] < max(i - k, 0):
                heapq.heappop(max_heap)
            cur_max = -max_heap[0][0] + nums[i]
            heapq.heappush(max_heap, (-cur_max, i))
        return cur_max


class Solution3:
    def maxResult(self, nums: List[int], k: int) -> int:
        """Monotonic stack to keep the largest value at the left of the window

        O(N), 1029 ms, faster than 94.81%
        """
        monostack = deque([(nums[0], 0)])
        cur_max = nums[0]
        for i in range(1, len(nums)):
            while monostack[0][1] < i - k:
                monostack.popleft()
            cur_max = nums[i] + monostack[0][0]
            while monostack and monostack[-1][0] < cur_max:
                monostack.pop()
            monostack.append((cur_max, i))
        return cur_max


sol = Solution3()
tests = [
    ([1,-1,-2,4,-7,3], 2, 7),
    ([10,-5,-2,4,0,3], 3, 17),
    ([1,-5,-20,4,-1,3,-6,-3], 2, 0),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.maxResult(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
