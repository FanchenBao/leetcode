# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def addDigits(self, num: int) -> int:
        """LeetCode 258

        46 ms, faster than 6.65% 
        """
        while num // 10:
            tmp = 0
            while num:
                q, r = divmod(num, 10)
                tmp += r
                num = q
            num = tmp
        return num


class Solution2:
    def addDigits(self, num: int) -> int:
        """From the official solution, math approach
        """
        if num == 0:
            return 0
        r = num % 9
        return r if r else 9


sol = Solution2()
tests = [
    (38, 2),
    (0, 0),
]

for i, (num, ans) in enumerate(tests):
    res = sol.addDigits(num)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
