# from pudb import set_trace; set_trace()
from typing import List
import heapq
import math


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        """LeetCode 1675

        First step is to multiply all the odd numbers by two. This is because
        all odd values can ONLY be multipled once. So let's just do that once.
        Afterwards, we will focus on reducing the max value, while keeping an
        eye on the max deviation. Note that if an odd value is not supposed to
        be doubled, it will be reduced by half during the process of reducing
        the max values.

        One key element to note is that during reduction, it is possible that
        the min value of the array might change. If that happens, we simply
        update the min value. We will keep reducing the max until we hit a max
        that is odd.

        O(NlogN), 944 ms, 89% ranking.
        """
        for i, n in enumerate(nums):
            if n % 2:
                nums[i] *= -2
            else:
                nums[i] *= -1
        heapq.heapify(nums)
        min_n = max(nums)
        res = math.inf
        while True:
            max_n = heapq.heappop(nums)
            res = min(res, abs(max_n - min_n))
            if max_n % 2 == 0:
                max_n //= 2
                heapq.heappush(nums, max_n)
                min_n = max(min_n, max_n)
            else:
                break
        return res


sol = Solution()
tests = [
    ([1, 2, 3, 4], 1),
    ([4, 1, 5, 20, 3], 3),
    ([2, 10, 8], 3),
    ([3, 5], 1),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.minimumDeviation(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
