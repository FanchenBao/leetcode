# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_right


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        """LeetCode 456

        Failed to solve this one.
        The following method is copied from my previous attempt at this problem
        more than a year ago. Interestingly, that time I was able to solve this
        problem using less efficient method. Yet I was not able to do the same
        this time.

        The key idea is that we go from left to right and keep track of the
        lowest valley reachable at each position. For instance, vs[i] records
        the lowest value from 0 to i. Then we go from right to left and keep
        record of the possible third values in a monotonic stack, such that all
        the values in the stack are larger than vs[j]. This means all the
        potential third values from j to the end are stored in the stack. Then
        for each new nums[j] going from right to left, we compare it to the
        top of the stack. If nums[j] is bigger, we have found the 132 pattern.
        Otherwise, we add nums[j] to the stack, as it is potentially a third
        value for elements we haven't checked yet.

        O(N), 342 ms, faster than 96.36%
        """
        stack = []
        vs = []
        # record all the valleys from 0 to i
        for n in nums:
            if not vs or n < vs[-1]:
                vs.append(n)
            else:
                vs.append(vs[-1])
        for j in range(len(nums) - 1, -1, -1):
            # make sure everything in the stack is larger than vs[j]
            # thus all of them can serve as the third value with respect
            # to vs[j] as the first value
            while stack and stack[-1] <= vs[j]:
                stack.pop()
            if not stack or nums[j] <= stack[-1]:
                stack.append(nums[j])  # potentially a third value
            else:
                # current value is larger than some third value, which
                # guarantees that it is also larger than vs[j] (because all
                # third values are larger than vs[j]). We have found the
                # pattern
                return True
        return False


sol = Solution()
tests = [
    ([1,2,3,4], False),
    ([3, 1, 4, 2], True),
    ([-1,3,2,0], True),
    ([3,5,0,3,4], True),
    ([-2,1,1], False),
    ([1, 1, 2, 1], False),
    ([1,2,3,4,-4,-3,-5,-1], False),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.find132pattern(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
