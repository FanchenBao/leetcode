# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """LeetCode 342

        Binary of n must have one '1' at the MSB, and even number of trailing
        '0'.

        48 ms, faster than 59.25% 
        """
        bstr = bin(n)[2:]
        return bstr[0] == '1' and bstr.count('0') == len(bstr) - 1 and len(bstr) % 2


sol = Solution()
tests = [
    (16, True),
    (5, False),
    (1, True),
    (2, False),
]

for i, (n, ans) in enumerate(tests):
    res = sol.isPowerOfFour(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
