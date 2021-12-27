# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def findComplement(self, num: int) -> int:
        """LeetCode 476

        Find the mask specific to num and then XOR.

        O(1), 32 ms, 55% ranking.
        """
        return num ^ ((1 << (len(bin(num)) - 2)) - 1)


sol = Solution()
tests = [
    (5, 2),
    (1, 0),
    (0, 1),
]

for i, (num, ans) in enumerate(tests):
    res = sol.findComplement(num)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
