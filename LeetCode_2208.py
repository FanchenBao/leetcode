# from pudb import set_trace; set_trace()
from typing import List
import heapq


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        """In order to reduce as much as possible for each step, we must pick
        the currently largest value for halving. This means we need to keep
        a max heap on the numbers. Each time, we halve the largest value, and
        put the remaining value back to the heap. Keep doing this until the
        amount of reduction is larger or equal to half of the original sum.

        O(NlogN), 1366 ms, faster than 65.45%
        """
        heap = [-n for n in nums]
        heapq.heapify(heap)
        tgt = sum(nums) / 2
        red, steps = 0, 0
        while heap:
            cur_max = -heapq.heappop(heap)
            red += cur_max / 2
            steps += 1
            if red >= tgt:
                return steps
            heapq.heappush(heap, -cur_max / 2)


sol = Solution()
tests = [
    ([5,19,8,1], 3),
    ([3,8,20], 3),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.halveArray(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
