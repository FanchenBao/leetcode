# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        """
        I used a bunch of good test cases to figure out all the edge cases.
        
        30 ms, faster than 86.00% 
        """
        if purchaseAmount % 10 == 0:
            return 100 - purchaseAmount
        upper = (purchaseAmount // 10 + 1) * 10
        lower = purchaseAmount // 10 * 10
        if upper - purchaseAmount <= purchaseAmount - lower:
            return 100 - upper
        return 100 - lower


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
