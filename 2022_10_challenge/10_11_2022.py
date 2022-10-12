# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """LeetCode 334

        I thought this problem was easy. Monotonic array, and we are done.
        However, there is an evil twist, such as the test case

        [9,10,5,11,10,9,8]

        Just doing monotonic array would miss the test case above, because
        when 5 knocks out everything in the array, we are losing candidates.

        Generally speaking, if the current n replaces only one value in the
        monotonic array, it's fine. We are not losing anything, and in fact,
        we are gaining, because we use a smaller middle value to replace a
        previous middle value.

        However, if the current n replaces both values in the monotonic array,
        we have a net loss of one value. This could be deadly. Therefore, the
        solution is to keep track of the smallest middle value in the past
        when the monotonic array hits length of two. And for each new n, we
        first check if n is bigger than the previous smallest middle value. If
        it is, then we have an answer already. Otherwise, we do the monotonic
        array business.

        O(N) 724 ms, faster than 78.32%
        """
        stack = []
        pre_mid = math.inf
        for n in nums:
            if len(stack) == 2:
                pre_mid = min(pre_mid, stack[-1])
            if n > pre_mid:
                return True
            while stack and n <= stack[-1]:
                stack.pop()
            stack.append(n)
            if len(stack) == 3:
                return True
        return False


class Solution2:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """This is essentially still monotonic stack, but the big big
        difference is that we don't pop everything if the current value is
        smaller than stack[0]. With no popping but only replacing, we make sure
        that any build up of the stack previously won't be lost just because
        we have updated the smallest value.
        """
        stack = [math.inf, math.inf]
        for n in nums:
            if n <= stack[0]:
                stack[0] = n
            elif n <= stack[1]:
                stack[1] = n
            else:
                return True
        return False


sol = Solution2()
tests = [
    ([1,2,3,4,5], True),
    ([5,4,3,2,1], False),
    ([2,1,5,0,4,6], True),
    ([20,100,10,12,5,13], True),
    ([1,2,1,3], True),
    ([9,10,5,11,10,9,8], True),
    ([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], False),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.increasingTriplet(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
