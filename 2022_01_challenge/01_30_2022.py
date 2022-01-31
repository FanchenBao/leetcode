# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        LeetCode 189

        The naive solution is very simple, but to make it O(1) extra space and
        O(N) time, it is not as easy. The idea below uses swap, and at each
        step, we swap smaller than half of the remaining numbers (i.e the
        numbers that still haven't been completely resettled). If the target
        numbers are smaller than half the total length, we swap all of them.
        Otherwise, we only swap the beginning of the target. Each round, we
        use the same logic to handle the situation, until the target to swap
        shrinks down to length zero.

        O(1) space and O(N) time. 441 ms, 23% ranking.
        """
        N = len(nums)
        k %= N
        left = 0
        while k:
            if k <= N // 2:
                for i in range(left, left + k):
                    nums[i], nums[-k + i - left] = nums[-k + i - left], nums[i]
                left += k
                N -= k
            else:
                to_move = N - k
                for i in range(left, left + to_move):
                    nums[i], nums[i + to_move] = nums[i + to_move], nums[i]
                left += to_move
                N -= to_move
                k -= to_move
            k %= N


class Solution2:

    def rotate(self, nums: List[int], k: int) -> None:
        """three reverses. A smart idea I came up with when I encountered this
        problem the first time. It is a shame that I wasn't able to think about
        it this time.

        277 ms, 51% ranking.
        """
        def rev(lo: int, hi: int) -> None:
            while lo < hi:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo += 1
                hi -= 1

        N = len(nums)
        k %= N
        rev(0, N - 1)
        rev(0, k - 1)
        rev(k, N - 1)


sol = Solution2()
tests = [
    ([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]),
    ([-1,-100,3,99], 2, [3,99,-1,-100]),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.rotate(nums, k)
    if nums == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {nums}')
