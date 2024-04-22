# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        cycles = []
        N = len(receiver)
        dp = [[-1, -1, -1] for _ in range(N)]  # dp[i] = [k pass score, cycle index, index within cycle]

        def helper(int i) -> int:
            if dp[i][0] >= 0:
                return dp[i][0]
            stack = []
            cur = i
            while receiver[cur] >= 0:
                stack.append(cur)
                nex = receiver[cur]
                receiver[cur] = -1
                cur = nex
            j = len(stack) - 1
            while j >= 0 and stack[j] != cur:
                j -= 1
            cycles.append(stack[j:])





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
