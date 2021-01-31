# from pudb import set_trace; set_trace()
from typing import List
import bisect
import math
import heapq


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        """I wasn't able to solve this problem by myself.

        This is the WRONG idea using DP:
        At each position in nums, we can expand all the
        choices. And for each number, we pick the best possible path onward. If
        we work from the last position back to the front, then we will have the
        best option calculated at the front. For instance, given

        [2, 10, 8], I can expand it to

        1  5   1
        2  10  2
               4
               8

        So I would go from position 1, which is [5, 10]. For 5, the best option
        is 4 in position 2. So I record the min difference going from 5 to the
        last position as 1. For 10, we choose 8, so the min diff for 10 is 2.
        Then we work on [1, 2]. For 1, we choose 5 with diff max(4, 1) = 4.
        For 2, we also choose 5 with diff max(3, 1) = 3. So the final answer is
        the min of the diff in position 0, which is 3.

        Now, this DP idea doesn't work. A counter example is [4, 12, 312]. You
        can try it yourself.

        Basically, this problem cannot be approached with DP, because the
        problem is not completely dependent on the optimal solution of the sub-
        problems.

        I eventually have to check the hints, which pointed out that I shall
        find the min posible values at each position, and incrementally double
        the min value and recompute the overall diff, until there is a min value
        that cannot be doubled. It works because, as the hint points out, if
        the current solution is not the optimal, then we must have the optimal
        solution with its min value larger than our current min value.

        We also need to use heapq to facilitate the searching of the min value.

        O(NlogN), 1068 ms, 35% ranking.
        """
        # pg contains the min possible values (and their index) for the given
        # nums
        pq, max_n, res = [], -math.inf, math.inf
        for i, n in enumerate(nums):
            if n % 2:
                heapq.heappush(pq, (n, i))
            else:
                while n % 2 == 0:
                    n //= 2
                heapq.heappush(pq, (n, i))
            max_n = max(max_n, n)
        while True:
            cur_min, i = heapq.heappop(pq)
            res = min(res, max_n - cur_min)  # update current diff
            # The criteria for determining whether the current min can be
            # doubled: 1. it is odd, 2. it is even and doubling it is within
            # the limit.
            if cur_min % 2 or 2 * cur_min <= nums[i]:
                cur_min *= 2
                heapq.heappush(pq, (cur_min, i))
                max_n = max(max_n, cur_min)
            else:
                break
        return res


sol = Solution()
tests = [
    ([4, 1, 5, 20, 3], 3),
    ([1, 2, 3, 4], 1),
    ([2, 10, 8], 3),
    ([4, 12, 312], 35),
    ([3, 5], 1)
]

for i, (nums, ans) in enumerate(tests):
    res = sol.minimumDeviation(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
