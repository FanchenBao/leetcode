# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        def solve(d1, d2, c1, c2):
            print('############')
            # handles uniqueCnt 1
            k, r = divmod(c1, d1 - 1)
            next_start = k * d1 + r + int(r != 0)  # next start for d2
            print(f'{k=}, {r=}, {next_start=}')

            # handle uniqueCnt 2
            g = math.gcd(d1, d2)
            coprime2 = d2 // g
            # remove the number of values not taken from 1 to next_start - 1
            # but can be taken in d2 from c2. This is to make sure that we take
            # full advantage of all the values from 1 to next_start - 1
            rem2 = (c2 - (k - 1 - (k - 1) // coprime2)) if k > 0 else c2
            # If after taking full advantage, we already fulfill the requirement
            # of c2, then the largest value under d1 is the answer
            print(f'{coprime2=}, {rem2=}')
            if rem2 <= 0:
                return next_start - 1
            
            if next_start % d2 == 0:
                next_start += 1
            # otherwise, we first find the number of values to take from
            # next_start to the immediate next multiple of d2
            next_mult_d2 = (next_start // d2 + 1) * d2
            # If there is enough values in this gap, we have found the largest
            # value under d2.
            print(f'{next_mult_d2=}')
            if rem2 - (next_mult_d2 - next_start) <= 0:
                return next_start + rem2 - 1

            # Otherwise, we redo the same thing as d1.
            rem2 -= (next_mult_d2 - next_start)
            print(f'{rem2=}')
            k, r = divmod(rem2, d2 - 1)
            coprime1 = d1 // g
            pot_swap = k - 1 - (k - 1) // coprime1
            end = k * d2 + next_mult_d2 + r - int(r == 0)
            print(f'{k=}, {r=}, {end=}')
            print('*************')
            return end

        return min(
            solve(divisor1, divisor2, uniqueCnt1, uniqueCnt2),
            solve(divisor2, divisor1, uniqueCnt2, uniqueCnt1),
        )


sol = Solution()
tests = [
    # (2, 7, 1, 3, 4),
    # (3, 5, 2, 1, 3),
    # (2, 4, 8, 2, 15),
    (16, 14, 12, 8, 20),
]

for i, (divisor1, divisor2, uniqueCnt1, uniqueCnt2, ans) in enumerate(tests):
    res = sol.minimizeSet(divisor1, divisor2, uniqueCnt1, uniqueCnt2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
