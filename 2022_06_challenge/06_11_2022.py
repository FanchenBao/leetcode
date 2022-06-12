# from pudb import set_trace; set_trace()
from typing import List
from bisect import bisect_right
from itertools import accumulate
import math


class Solution1:
    def minOperations(self, nums: List[int], x: int) -> int:
        """LeetCode 1658

        I don't think this is an easy one. My previous attempt at this problem
        was Jan, 2021. It was quite bad. So I am genuinely glad that I am able
        to solve it with only one mistake. The idea is that we produce a prefix
        sum on nums. This can tell us whether we can add up some values on the
        left to reach x. If we can, we record the length. Then, we mentally
        append the entire array to the right and continue the prefix sum. This
        gives us a new_presum that is twice the length of nums. Say N =
        len(nums). Now we need to start from new_presum[N - 1] and going to the
        right. Each time, we compute new_presum[i] - x, and see if this value
        is in any of the values to the left in new_presum. If it is, then we
        have found another valid sets of operations to reach x. Continue to do
        this until we have gone beyond new_presum[N - 1].

        In implementation, we can definitely do the append and use binary
        search to find whethe new_presum[i] - x is in the new_presum array.
        However, this is not necessary, because each value in presum is unique
        which means we can use a index dict to match value to its index. With
        this, we can search for the index of new_presum[i] - x in O(1) time

        O(N), 1437 ms, faster than 66.75% 
        """
        if nums[0] > x and nums[-1] > x:
            return -1
        presum_dict = {}
        res = math.inf
        for i, ps in enumerate(accumulate(nums)):
            if ps == x:
                res = min(res, i + 1)
            presum_dict[ps] = i
        if ps < x:  # sum of all nums cannot match x
            return -1
        N = len(nums)
        presum_limit = ps
        i = N - 1
        while ps - x < presum_limit:
            res = min(res, i - presum_dict.get(ps - x, -math.inf))
            ps += nums[i - N + 1]
            i += 1
        return -1 if res > N else res


class Solution2:
    def minOperations(self, nums: List[int], x: int) -> int:
        """This is the official solution recorded by myself in the previous
        attempt at this problem. The idea is generally the same, but it has a
        smarter and simpler implementation.

        If some values at the front and back add up to x, that means the values
        in the middle must add up to sum(nums) - x. Our goal is to use prefix
        sum to find which range of nums adds up to sum(nums) - x, and we want
        the largest range (so that the length of the front and back is
        minimized).
        """
        if nums[0] > x and nums[-1] > x:
            return -1
        presum_dict = {0: -1}
        target = sum(nums) - x
        ps, res, N = 0, math.inf, len(nums)
        for i, n in enumerate(nums):
            ps += n
            presum_dict[ps] = i
            if ps - target in presum_dict:
                res = min(res, N - i + presum_dict[ps - target])
        return res if res <= N else -1


        
sol = Solution2()
tests = [
    ([1,1,4,2,3], 5, 2),
    ([5,6,7,8,9], 4, -1),
    ([3,2,20,1,1,3], 10, 5),
    ([8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309], 134365, 16),
]

for i, (nums, x, ans) in enumerate(tests):
    res = sol.minOperations(nums, x)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
