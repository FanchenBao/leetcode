# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def findMin(self, nums: List[int]) -> int:
        """LeetCode 154

        It's obvious that the solution must be binary search. The most
        confusing part is when nums[lo] == nums[mid] == nums[hi], because this
        does not determine if the min is on the left or right side. Hence, when
        this happens, we always move lo forward. This ensures that each time
        a comparison with nums[mid] is made, it's guaranteed that we will know
        where the min is located.

        There are two situations when nums[mid] >= nums[lo]. One is that
        nums[mid] <= nums[hi]. This means lo, mid, hi is on the same rising edge
        which means we can return nums[lo] immediately. The other is nums[mid] >
        nums[hi]. This means the min value must be on the right half.

        When nums[mid] < nums[lo], then it is certain that the min value is on
        the left half.

        O(logN) on average, but the worst case will be O(N). 73 ms, 32% ranking.
        """
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            while lo < hi and nums[lo] == nums[hi]:
                lo += 1
            mid = (lo + hi) // 2
            if nums[lo] <= nums[mid]:
                if nums[mid] <= nums[hi]:
                    return nums[lo]
                lo = mid + 1
            else:
                hi = mid
        return nums[hi]


class Solution2:
    def findMin(self, nums: List[int]) -> int:
        """This is the most common solution. It's basically the same concept.
        When the difficult-to-decide situation arises, we move the pointer one
        by one to get out of the undeterministic state.

        This solution is better than Solution1, because even if we are hit by
        the ambiguous case, we are able to make quick jumps in the subsequent
        comparisons. In Solution1, each ambiguous case requires the elimination
        of all ambiguous values one by one.

        E.g.

        33333...312.....3

        In Solution1, we will move lo one at a time until all the leading 3s are
        elimiated. This times a long time. In Solution2, we simply move hi one
        spot forward, then in the next comparison, nums[mid] is not the same as
        nums[hi], and we can do bigger jumps.


        O(logN), 52 ms
        """
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            elif nums[mid] < nums[hi]:
                hi = mid
            else:
                hi -= 1
        return nums[hi]


sol = Solution2()
tests = [
    ([1, 3, 5], 1),
    ([2, 2, 2, 0, 1], 0),
    ([1, 3, 3], 1),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.findMin(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
