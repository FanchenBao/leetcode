# from pudb import set_trace; set_trace()
from typing import List
from random import choice


class Solution1:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        LeetCode 75

        Two pointers at either end. The goal is to sort 0 and 2. When these two
        are sorted, the remaining is sorted as well. We run the same algorithm
        twice. The first time, we put 0 in place. We keep moving hi until
        0 is encountered. Then we swap with lo. The second time, we put 2 in
        place. We keep moving lo until 2 is encountered. Then we swap with hi.

        O(2N), 32 ms, 83 % ranking.

        However, this is two-pass, so technically not satisfying the requirement.
        """
        N = len(nums)
        lo, hi = 0, N - 1
        while lo < hi:
            while lo < N and nums[lo] == 0:
                lo += 1
            while hi >= 0 and nums[hi] != 0:
                hi -= 1
            if lo < hi:
                nums[lo], nums[hi] = nums[hi], nums[lo]
        lo, hi = 0, N - 1
        while lo < hi:
            while lo < N and nums[lo] != 2:
                lo += 1
            while hi >= 0 and nums[hi] == 2:
                hi -= 1
            if lo < hi:
                nums[lo], nums[hi] = nums[hi], nums[lo]


class Solution2:
    def sortColors(self, nums: List[int]) -> None:
        """One-pass, O(N)

        We use a third pointer mi to handle the case such as [1,1,0,1,1]. In
        solution1, we handle this case by going through the nums two times.
        """
        N = len(nums)
        lo, hi, mi = 0, N - 1, -1
        while lo < hi and mi < hi:
            while lo < hi and nums[lo] == 0:
                lo += 1
            while lo < hi and nums[hi] == 2:
                hi -= 1
            if nums[lo] == 2 or nums[hi] == 0:
                nums[lo], nums[hi] = nums[hi], nums[lo]
            else:
                if mi < 0:
                    mi = lo
                while mi < hi and nums[mi] == 1:
                    mi += 1
                if nums[mi] == 0:
                    nums[lo], nums[mi] = nums[mi], nums[lo]
                else:
                    nums[hi], nums[mi] = nums[mi], nums[hi]


class Solution3:
    def sortColors(self, nums: List[int]) -> None:
        """One-pass, O(N), 94% ranking.

        Another three pointers, but better implementation. Note that when
        nums[mi] == 0, we swap and increment both lo and mi. To show that we
        can do this, let's see the three starting scenarios.

        1. nums[0] == 0. Since lo == mi == 0, we do a dummy swap, and both
        increment to 1. No issue.
        2. nums[0] == 1. lo will stay put, mi will advance. As mi advance, if
        nums[mi] == 0, it swaps with nums[lo], which currently points to 1.
        After swap, we can increment both lo and mi, because nums[mi] now points
        to 1.
        3. nums[0] == 2, we swap with hi, and go back to the previous two
        scenarios.
        """
        N = len(nums)
        lo, hi, mi = 0, N - 1, 0
        while mi <= hi:
            if nums[mi] == 0:
                nums[lo], nums[mi] = nums[mi], nums[lo]
                lo += 1
                mi += 1
            elif nums[mi] == 2:
                nums[hi], nums[mi] = nums[mi], nums[hi]
                hi -= 1
            else:
                mi += 1


sol = Solution3()
num_tests = 100
length = 300
tests = [[choice([0, 1, 2]) for _ in range(length)] for _ in range(num_tests)]

for i, nums in enumerate(tests):
    res = nums[:]
    sol.sortColors(res)
    ans = sorted(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}, Test: {nums}')
