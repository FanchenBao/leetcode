# from pudb import set_trace; set_trace()
from typing import List, Tuple
from functools import lru_cache
import itertools


class Solution1:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """TLE. DP solution, O(NK)"""
        n = len(nums)
        zi = []
        for i in range(n):
            if nums[i] == 1:
                nums[i] += (nums[i - 1] if i > 0 else 0)
            else:
                zi.append(i)
        m = len(zi)
        if m <= k:
            return n

        @lru_cache(maxsize=None)
        def helper(idx, flippable) -> Tuple[int, int]:
            if idx == m:
                return (0, 0) if zi[-1] == n - 1 else (nums[-1], nums[-1])
            max_from_start = nums[zi[idx] - 1] if zi[idx] > 0 else 0
            max_overall = max_from_start
            if flippable > 0:
                max_from_start_flip, max_overall_flip = helper(idx + 1, flippable - 1)
                max_from_start += 1 + max_from_start_flip
                max_overall = max([max_overall, max_from_start, max_overall_flip])
            max_from_start_no, max_overall_no = helper(idx + 1, flippable)
            max_overall = max([max_overall, max_from_start, max_overall_no])
            return max_from_start, max_overall

        _, res = helper(0, k)
        return res


class Solution2:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """LeetCode 1004

        Greedy solution with sliding window implementation. The greedy idea
        is like this: considering each stretch of 1s as island and the 0s as
        gaps. The best strategy is to fill in each gap such that the islands can
        be joined. We can prove this by assuming a solution where some gap is
        not completely flipped while we still can. In this case, any max islands
        can be further extended by flipping the 0s on its edge. Therefore, the
        optimal strategy is to always concatenate islands as much as we can.

        Thus, we use a sliding window idea. We turn nums into counts of 0s and
        1s. We try to flip all the 0s going to the right, as much as we can.
        Once we cannot go any further, we record the current result. Then we
        remove the flippable on the left and give it to the right. We continue
        this until the entire list is covered.

        The implementation itself is very convoluted. I don't like it at all.

        O(N), 548 ms, 95% ranking.
        """
        counts = [len(list(g)) for _, g in itertools.groupby(nums)]
        if nums[0] == 0:
            counts = [0] + counts
        left, right = 1, 1
        window, res = counts[0], 0
        flippable = k
        while right < len(counts):
            already_flipped = 0
            while right < len(counts):
                flipped = min(counts[right], flippable)  # flip as many as we can
                flippable -= flipped
                window += flipped  # grow sliding window from the flipped 0s
                if flipped == counts[right]:  # current gap completely filled
                    window += counts[right + 1] if right < len(counts) - 1 else 0
                    right += 2
                    already_flipped = 0
                else:  # current gap cannot be filled
                    already_flipped = flipped
                    break
            # Note that we can include flippable in the winodow if we have
            # exhausted the list, and there are 0s to the left of left for us
            # to place the extra flippable.
            res = max(res, window + (flippable if left - 2 > 0 else 0))
            if left == right:  # if the gap is bigger than k, we shrink the gap to k
                counts[right] = k
                flippable = k
                window = 0
            else:  # sliding window. Remove from left and add to the right
                window -= (counts[left] + counts[left - 1] + already_flipped)
                flippable += (counts[left] + already_flipped)
                left += 2
        return res


class Solution3:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """Much simpler implementation, courtesy of:

        https://leetcode.com/problems/max-consecutive-ones-iii/discuss/1304328/Python-Sliding-window-solution-explained

        The idea is the same as solution2, but expressed in a much nicer way.
        Our goal is to find the longest subarray of nums such that there are
        k zeros in the subarray. This can be resolved using sliding window.
        """
        left, right, res, zeros = 0, 0, 0, 0
        n = len(nums)
        while right < n:
            while right < n:
                if nums[right] == 0:
                    if zeros == k:
                        break
                    zeros += 1
                right += 1
            res = max(res, right - left)
            while left < n and nums[left] == 1:
                left += 1
            left += 1  # shrink 0s one by one
            zeros -= 1
        return res


class Solution4:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """Same as solution4, but better implementation."""
        left, right, res, zeros = 0, 0, 0, 0
        while right < len(nums):
            if zeros + (nums[right] == 0) <= k:
                zeros += (nums[right] == 0)
                right += 1
                res = max(res, right - left)
            else:
                zeros -= (nums[left] == 0)
                left += 1
        return res


sol = Solution4()
tests = [
    ([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2, 6),
    ([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3, 10),
    ([0, 0, 0, 1], 4, 4),
    ([0, 0, 1, 1, 1, 0, 0], 0, 3),
    ([1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1], 8, 25),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.longestOnes(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
