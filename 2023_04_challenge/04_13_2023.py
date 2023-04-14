# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """LeetCode 946

        Each time the top of the stack matches the current popped, we must pop.
        Otherwise, we push new values from pushed, until there is nothing to
        push anymore. By that time, we shall have popped everything. If not, it
        is not possible.

        O(N), 68 ms, faster than 87.13%
        """
        stack = []
        i = j = 0
        N = len(popped)
        while j < N:
            while stack and popped[j] == stack[-1]:
                stack.pop()
                j += 1
            if i < N:
                stack.append(pushed[i])
                i += 1
            else:
                break
        return i == N and j == N and not stack


class Solution2:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """From the official solution. Better implementation but the same idea.
        """
        stack = []
        j = 0
        for p in pushed:
            stack.append(p)
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return j == len(popped)
        

sol = Solution2()
tests = [
    ([1,2,3,4,5], [4,5,3,2,1], True),
    ([1,2,3,4,5], [4,3,5,1,2], False),
]

for i, (pushed, popped, ans) in enumerate(tests):
    res = sol.validateStackSequences(pushed, popped)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
