# from pudb import set_trace; set_trace()
from typing import List
import math


class BrowserHistory:

    def __init__(self, homepage: str):
        """LeetCode 1472

        Straightforward solution.

        214 ms, faster than 91.17%
        """
        self.history = [homepage]
        self.cur = 0
        self.end = 0

    def visit(self, url: str) -> None:
        self.cur += 1
        self.end = self.cur
        if self.cur == len(self.history):
            self.history.append(url)
        else:
            self.history[self.cur] = url

    def back(self, steps: int) -> str:
        self.cur = max(0, self.cur - steps)
        return self.history[self.cur]

    def forward(self, steps: int) -> str:
        self.cur = min(self.end, self.cur + steps)
        return self.history[self.cur]
        

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
