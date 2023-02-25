# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        """LeetCode 1675, failed

        Unable to solve it this time. I did solve it two times in the past, so
        it is quite unusual.

        I saw the hint. Basically, we reduce all numbers in nums to its minimum
        state, i.e., we divide all the even numbers by two until they become odd

        Then we can compute the min difference under minimum of max value. We
        do this by doubling the min (if it's possible). If by doing so, we
        obtain a new a max. Then we are computing the min difference under the
        second minimun of max value.

        Keep doing this, we will be computing the min difference under the
        smallest, second smallest, third smallest, etc. max value. We stop until
        we cannot double the min, which means we have reached the largest min
        possible. Although the max can keep going, we won't be able to achieve
        any better difference. Hence, this operation produces the smallest
        difference.

        O(NlogN), 3475 ms, faster than 20.90% 
        """
        min_heap = []
        cur_max = 0
        for i, n in enumerate(nums):
            while n % 2 == 0:
                n //= 2
            heapq.heappush(min_heap, (n, i))
            cur_max = max(cur_max, n)
        res = math.inf
        while min_heap[0][0] % 2 == 1 or min_heap[0][0] < nums[min_heap[0][1]]:
            res = min(res, cur_max - min_heap[0][0])
            n, i = heapq.heappop(min_heap)
            heapq.heappush(min_heap, (n * 2, i))
            cur_max = max(cur_max, n * 2)
        return min(res, cur_max - min_heap[0][0])



sol = Solution()
tests = [
    ([1,2,3,4], 1),
    ([4,1,5,20,3], 3),
    ([2,10,8], 3),
    ([3,5], 1),
    ([10,4,3], 2),
    ([2,8,6,1,6], 1),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.minimumDeviation(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
