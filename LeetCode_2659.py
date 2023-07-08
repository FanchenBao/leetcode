# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        """Fail.

        A good explanation is here: https://leetcode.com/problems/make-array-empty/discuss/3466731/Just-sort-without-any-other-tricky-data-structures.

        First of all, the total number of removals will cost len(nums) of steps.
        This is a hard minimum. We cannot get below that.

        Any additional cost is due to relocation of the values. Thus, we need to
        find out the number of relocations necessary to remove each value.

        Notice that to remove a consecutive smallest stretch of values, we can
        relocate all the values larger than the largest of the stretch to return
        the array into its original position.

        For instance: [a, 3, b, 0, c, d, 1, e, 2] (where the letters represent
        some values larger than 3)

        To remove [0, 1, 2], which is a smallest consecutive stretch, we need to
        move [a, 3, b], [c, d], and [e] to the right. After the removal of
        [0, 1, 2], we have [a, 3, b, c, d, e], which follows the exact same
        positions as the original array, except for the removal of [0, 1, 2].

        Interestingly, if we have this case:

        [a, 3, b, 0, c, d, 1, e, 2, f, g, h], we can remove [0, 1, 2] by turning
        the array into this:

        [f, g, h, a, 3, b, c, d, e]

        We are NOT relocating all the values larger than 2, because it is not
        necessary to relocate [f, g, h] to remove [0, 1, 2]. However, to remove
        [3], [f, g, h] have to be relocated no matter what, because they are
        larger than 3. So we either relocate them in the next round of removing
        [3], or we relocate them in the previous round of removing [0, 1, 2].
        The effect is the same. But the implication is quite different. Because
        if we relocate them in the previous round, we significantly simplify the
        logic of each round of relocation: we relocate all the numbers with
        value larger than the largest of the smallest consecutive stretch.

        With this method, we can solve the problem by sorting the original array
        with their indices attached. If we see a stretch of smallest values (this
        means their indices increases), we do nothing. Once a value has smaller
        index than its predecessor, that is the signal that the previous stretch
        can be removed. And the number of relocations is the number of values
        larger or equal to the current value.

        O(NlogN), 773 ms, faster than 50.58%
        """
        sorted_nums = sorted((n, i) for i, n in enumerate(nums))
        res = len(nums)  # the cost of removal
        # compute the cost of relocation
        for i in range(1, len(nums)):
            if sorted_nums[i][1] < sorted_nums[i - 1][1]:  # not a stretch
                res += len(nums) - i
        return res


sol = Solution()
tests = [
    ([3,4,-1], 5),
    ([1,2,4,3], 5),
    ([1,2,3], 3),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.countOperationsToEmptyArray(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
