# from pudb import set_trace; set_trace()
from typing import List
import math
from itertools import groupby


class Solution1:
    def longestSubarray(self, nums: List[int]) -> int:
        """LeetCode 1493

        Group all the consecutive 1s and 0s together and count them. Then
        iterate through each group and count. If we find a group of 0 and of
        length 1, we can delete that zero and combine the groups of 1s on both
        sides.

        The tricky case is when we don't have any single 0s to delete. Thus, we
        need to set up a flag to indicate whether delete has happen. This also
        helps when there is no 0s in the nums, in which case we must delete one
        1.

        O(N), 340 ms, faster than 97.91% 
        """
        counts = [(k, len(list(g))) for k, g in groupby(nums)]
        res = 0
        has_delete = False
        for i, (k, l) in enumerate(counts):
            if k == 1:
                res = max(res, l)
            else:
                has_delete = True
                if 0 < i < len(counts) - 1 and l == 1:
                    res = max(res, counts[i - 1][1] + counts[i + 1][1])
        return res if has_delete else res - 1


class Solution2:
    def longestSubarray(self, nums: List[int]) -> int:
        """This is the sliding window solution from the official solution. The
        idea is to find the longest window such that there is no more than one
        0s inside the window. Then the answer is the longest such window minus
        one. We must minus one because one element must be removed.

        O(N), 421 ms, faster than 18.65%
        """
        res = lo = zero_count = 0
        for hi in range(len(nums)):
            zero_count += int(nums[hi] == 0)
            while zero_count > 1:
                zero_count -= int(nums[lo] == 0)
                lo += 1
            # the current window has at most 1 zero
            res = max(res, hi - lo)
        return res
        

# sol = Solution2()
# tests = [
#     ("hello", "holle"),
#     ("leetcode", "leotcede"),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
