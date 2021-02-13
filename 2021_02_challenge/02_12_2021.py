# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def numberOfSteps(self, num: int) -> int:
        """Straightforward solution. Just divide by two when it's even and minus
        1 when it's odd. Keep counting the steps.

        O(logN), 28 ms, 85% ranking.
        """
        res = 0
        while num:
            if num % 2:
                num -= 1
            else:
                num //= 2
            res += 1
        return res


class Solution2:
    def numberOfSteps(self, num: int) -> int:
        """A more computer-sciency solution, leveraging binary representation of
        the given number.
        O(logN), 32 ms, 63% ranking.
        """
        bstr = bin(num)[2:]
        return bstr.count('1') * 2 + bstr.count('0') - 1


sol = Solution2()
tests = [
    (14, 6),
    (8, 4),
    (123, 12),
]

for i, (num, ans) in enumerate(tests):
    res = sol.numberOfSteps(num)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
