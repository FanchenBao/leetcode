# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import deque


class Solution:
    def finalString(self, s: str) -> str:
        """
        Use a deque.

        O(N), 42 ms, faster than 78.16%
        """
        queue = deque()
        append_back = True
        for le in s:
            if le == "i":
                append_back = not append_back
            elif append_back:
                queue.append(le)
            else:
                queue.appendleft(le)
        res = "".join(queue)
        return res if append_back else res[::-1]


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
