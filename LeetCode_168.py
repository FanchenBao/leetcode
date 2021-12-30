# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def convertToTitle(self, columnNumber: int) -> str:
        """This is more complicated than I had expected. Basically, we perform
        divmod on columnNumber, and the subsequent quotient. At each divmod
        step, the remainder is used to determine the letter at the current
        position from right to left. The quotient is used for determining the
        next letter to the left.

        34 ms, 14% ranking.
        """
        res = ''
        q = columnNumber
        while q:
            q, r = divmod(q, 26)
            if r == 0:
                r, q = 26, q - 1
            res += chr(65 + r - 1)
        return res[::-1]


class Solution2:
    def convertToTitle(self, columnNumber: int) -> str:
        """Recursion version"""
        if columnNumber == 0:
            return ''
        q, r = divmod(columnNumber, 26)
        if r == 0:
            r, q = 26, q - 1
        return self.convertToTitle(q) + chr(65 + r - 1)


sol = Solution2()
tests = [
    (1, 'A'),
    (28, 'AB'),
    (701, 'ZY'),
]

for i, (columnNumber, ans) in enumerate(tests):
    res = sol.convertToTitle(columnNumber)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
