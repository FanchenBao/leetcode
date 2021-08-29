# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        """LeetCode 330

        I think this is greedy. Let's say we are currently looking at nums[i]
        and we know that after some patching, nums[0:i] can represent all the
        values from 1 to k. We call k the end range. If nums[i] is smaller or
        equal to k + 1, then we can incorporate nums[i] without any patching to
        have the end range reach at least k + 1. After incorporation, our new
        end range will be k + nums[i] (this is the most important insight). We
        can always expand the range just by adding the newly incorporated value
        to the previous end range.

        If nums[i] is bigger than k + 1, then our current range cannot cover the
        values from k + 1 to nums[i]. Therefore, we need to patch a value. Here,
        there are many ways to make the patch, because many values can be used
        as the patch to increase the current end range above nums[i]. However,
        there is only one value that can increase the range maximally, and that
        value is k + 1. In order to achieve minimum patch, we want each
        expansion of the range to be the largest possible. Therefore, we always
        patch k + 1 when k < nums[i].

        We continue expanding the end range until it is larger than the target
        n. Time complexity is O(M + logN), where M is the size of the input
        array and N is the target. 60 ms, 68% ranking.
        """
        res, idx = (1, 0) if nums[0] != 1 else (0, 1)
        end_range = 1
        while end_range < n:
            if idx < len(nums) and nums[idx] <= end_range + 1:
                end_range += nums[idx]
                idx += 1
            else:
                end_range += (end_range + 1)
                res += 1
        return res


sol = Solution()
tests = [
    ([1, 3], 6, 1),
    ([1, 5, 10], 20, 2),
    ([1, 2, 2], 5, 0),
]

for i, (nums, n, ans) in enumerate(tests):
    res = sol.minPatches(nums, n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
