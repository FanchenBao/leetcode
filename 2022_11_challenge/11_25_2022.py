# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """LeetCode 907

        We can pick any number in arr, and ask the question: how many subarrays
        that include this number also have this number as its smallest value.
        The answer is that we can put this number in the middle and extend left
        and right wards until we hit some value that is smaller than this number
        Then the maximum extension on the left and right are the range where
        the current number is the smallest in all the subarrays that include it.

        Given the example [3, 1, 2, 4]. For number 1, we have one value to its
        left and two values to its right that are all smaller than it. The total
        number of subarrays that include 1 can be thought of as the number of
        choices on the left multiplied by the number of choices on the right.
        The choices on the left is 1 + 1 = 2, because we can pick [3] or pick
        []. The number of choices on the right is 2 + 1 = 3, because we
        can choose [2], [2, 4], or []. Thus, the total number of subarrays that
        include 1 is 2 * 3 = 6. And the sum of these subarrays is 6 * 1 = 6.

        Similarly, we can perform the same trick for the other values.

        Now the question is how can we find out the number of values to the left
        and right that are smaller than the current number. The answer is
        monotonic increasing array. Each time we encounter a value that is
        smaller or equal to the top of the stack, it is guaranteed that the top
        of the stack is surounded on both sides by the immediate values that are
        smaller than it. If we include the indices in the array, it is trivial
        to find out the number of values smaller to the top of the array on its
        left and right.

        The solution follows this logic. We pre-populate the stack with [0, -1]
        to simplify the computation.

        O(N), 502 ms, faster than 90.57%
        """
        MOD = 10**9 + 7
        N = len(arr)
        stack = [[0, -1]]
        res = 0
        for i, a in enumerate(arr):
            while stack and stack[-1][0] >= a:
                v, idx = stack.pop()
                res = (res + (idx - stack[-1][1]) * (i - idx) * v) % MOD
            stack.append([a, i])
        while len(stack) > 1:
            v, idx = stack.pop()
            res = (res + (idx - stack[-1][1]) * (N - idx) * v) % MOD
        return res
        

sol = Solution()
tests = [
    ([3,1,2,4], 17),
    ([11,81,94,43,3], 444),
]

for i, (arr, ans) in enumerate(tests):
    res = sol.sumSubarrayMins(arr)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
