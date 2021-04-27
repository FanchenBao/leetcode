# from pudb import set_trace; set_trace()
from typing import List
# import numpy as np
import re
import math


class Solution1:
    def isPowerOfThree(self, n: int) -> bool:
        """LeetCode 326

        Using loop

        76 ms, 65% ranking
        """
        while n and not n % 3:
            n //= 3
        return n == 1


class Solution2:
    power_of_threes = set(3**p for p in range(20))

    def isPowerOfThree(self, n: int) -> bool:
        """Since there are only 19 power of threes available in the designated
        range of n, we can list them all

        76 ms
        """
        return n in self.power_of_threes


# class Solution3:
#     def isPowerOfThree(self, n: int) -> bool:
#         """Turn into base 3 and check whether the base 3 value consists of all
#         zeros except 1 in the first position. Use regex for the check

#         200 ms
#         """
#         return re.match(r'^10*$', np.base_repr(n, base=3))


class Solution4:
    def isPowerOfThree(self, n: int) -> bool:
        """Use log, but with addition of epsilon to avoid rounding error with
        floating number. e.g. log(243) / log(3) = 4.99999999 By addding an
        epsilon, we force the value to its correct form.
        """
        return n > 0 and 3**int(math.log(n) / math.log(3) + 10**(-5)) == n


class Solution5:
    max_power_three = 3**19

    def isPowerOfThree(self, n: int) -> bool:
        """Since 3 is prime, and the max power of 3 allowd is 3^19. If n is a
        power of 3, then 3^19 must be divided by n.

        This is a very brilliant solution taking advantage of 3 being prime.
        This is from the official solution.
        """
        return n > 0 and not self.max_power_three % n


sol = Solution1()
tests = [
    (27, True),
    (0, False),
    (9, True),
    (45, False),
    (243, True),
]

for i, (n, ans) in enumerate(tests):
    res = sol.isPowerOfThree(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
