# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def maximum69Number (self, num: int) -> int:
        """LeetCode 1323

        45 ms, faster than 77.64% 
        """
        lst = list(str(num))
        for i, n in enumerate(lst):
            if n == '6':
                lst[i] = '9'
                break
        return int(''.join(lst))


sol = Solution()
tests = [
    (9669, 9969),
    (9996, 9999),
    (9999, 9999),
]

for i, (num, ans) in enumerate(tests):
    res = sol.maximum69Number(num)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
