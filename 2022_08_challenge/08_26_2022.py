# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


class Solution:
    powers = set(''.join(sorted(str(1 << i))) for i in range(30))

    def reorderedPowerOf2(self, n: int) -> bool:
        """LeetCode 869

        Get all the powers of two, sort the num string, and put them in a set.
        Then we just need to check whether the sorted n string is in the set.

        54 ms, faster than 63.10% 

        UPDATE: only compute powers once. 28 ms, faster than 100.00%
        """
        
        return ''.join(sorted(str(n))) in self.powers
        

sol = Solution()
tests = [
    (1, True),
    (10, False),
]

for i, (n, ans) in enumerate(tests):
    res = sol.reorderedPowerOf2(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
