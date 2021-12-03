# from pudb import set_trace; set_trace()
from typing import List
from collections import namedtuple
import math


class Solution1:
    def maxProduct(self, nums: List[int]) -> int:
        """LeetCode 152

        I thought it was a straightforward Kardane's algo, but it turns out
        there is some work to do with regards to accumulating the negative and
        the positive. We cannot just keep tracking the positives, because if we
        have a giant negative previously, multiplying it with another negative
        will give us a giant positive value. Thus, we need to keep trakc of both
        negative and positive product of subarray ending at each position.

        Another trick is to handle the case of 0. Whenever 0 occurs, we
        basically have to start all over again.

        O(N), 64 ms, 32% ranking.
        """
        res = -math.inf
        Ele = namedtuple('Ele', 'pos,neg')
        cur = Ele(-math.inf, -math.inf)
        for n in nums:
            if n == 0:
                res = max(res, 0)
                cur = Ele(-math.inf, -math.inf)
            elif n > 0:
                cur = Ele(
                    n if cur.pos == -math.inf else cur.pos * n,
                    -math.inf if cur.neg == -math.inf else cur.neg * n,
                )
                res = max(res, cur.pos, cur.neg)
            else:
                cur = Ele(
                    -math.inf if cur.neg == -math.inf else cur.neg * n,
                    n if cur.pos == -math.inf else cur.pos * n,
                )
                res = max(res, cur.pos, cur.neg)
        return res


class Solution2:
    def maxProduct(self, nums: List[int]) -> int:
        """This is the same as the second solution I had more than a year ago.
        It has the same idea but with much better implementation.
        """
        res = cur_min = cur_max = nums[0]
        for n in nums[1:]:
            cur_min, cur_max = min(cur_min * n, cur_max * n, n), max(cur_max * n, cur_min * n, n)
            res = max(res, cur_max)
        return res


sol = Solution2()
tests = [
    ([2, 3, -2, 4], 6),
    ([-2, 0, -1], 0),
    ([-1,-2,-3,4,5,6,-3,-2,6,5,-4], 518400),
    ([-1,-2,-3], 6),
    ([-1,-2], 2),
    ([1], 1),
    ([-1], -1),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.maxProduct(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
