# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        LeetCode 739

        Use monotonic increasing stack. Build the result and the stack from
        right to left. The moment we can push the current value into the stack,
        the top of the stack is the first value that is larger than the current
        value. Or if there is no value in the stack after all the popping, the
        current value is the biggest so far.

        O(N), 900 ms, faster than 75.17%
        """
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if not stack:
                res[i] = 0
            else:
                res[i] = stack[-1] - i
            stack.append(i)
        return res


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
