# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        """LeetCode 665

        We use a stack to check for the number of peaks. This is the same
        method as in other problems where a non-decreasing array is to be
        created from a given array (think about all the water-holding problem).
        However, the trick in this problem is that in addition to considering
        peaks, we have to also consider valleys. When a single valley exists,
        the non-decreasing array method won't be able to detect it. Thus, we
        run another loop to check the number of valleys we have. This second
        run does not require a stack. We basically discard any value that is
        smaller than the previous value.

        O(N), 188 ms, 40% ranking.
        """
        stack = [-math.inf]
        count = 0
        # check for peaks
        for n in nums:
            while n < stack[-1]:
                stack.pop()
                count += 1
            if count > 1:
                break
            stack.append(n)
        if count <= 1:
            return True
        # check for valleys
        count = 0
        pre = -math.inf
        for n in nums:
            if n < pre:
                count += 1
                if count > 1:
                    break
            else:
                pre = n
        return count <= 1


class Solution2:
    def checkPossibility(self, nums: List[int]) -> bool:
        """Courtesy of https://leetcode.com/problems/non-decreasing-array/discuss/1190833/Python-O(n)-solution-explained

        The basic idea is to count and find where the last inversion happens. If
        there are two separate instances of inversion, we can immediately return
        False. If there is only one inversion, we need to examine whether this
        inversion happens to a single number, either being a peak or a valley.
        """
        p, n = -1, len(nums)
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                if p != -1:
                    return False
                p = i
        return p in [-1, 0, n - 2] or nums[p - 1] <= nums[p + 1] or nums[p] <= nums[p + 2]


sol = Solution2()
tests = [
    ([4, 2, 3], True),
    ([4, 2, 1], False),
    ([1, 3, 5, 6, 4, 4, 8, 8, 9, 10], False),
    ([1, 3, 5, 9, 9, 8, 8, 9, 10], False),
    ([1, 2, 3, 4], True),
    ([1, 2, 5, 3, 4, 1, 6], False),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.checkPossibility(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
