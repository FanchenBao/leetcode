# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        res = 0
        N = len(nums)
        state = [False] * (N + 1)
        for i in range(N):
            state[nums[i]] = True
            cur = 0
            for j in range(i + 1, N):
                k = nums[j]
                if state[k]:
                    res += cur
                elif not state[k - 1] and (k == N or not state[k + 1]):
                    cur += 1
                    res += cur
                elif state[k - 1] and state[k + 1]:
                    cur -= 1
                    res += cur
                else:
                    res += cur
            state.clear()
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
