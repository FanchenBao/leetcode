# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def bitwiseComplement(self, N: int) -> int:
        """Esta es un problema de categorica facil. No hay much de descutir"""
        return N ^ (1 << (len(bin(N)) - 2)) - 1


sol = Solution()
tests = [
    (5, 2),
    (7, 0),
    (10, 5),
    (0, 1),
]

for i, (N, ans) in enumerate(tests):
    res = sol.bitwiseComplement(N)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
