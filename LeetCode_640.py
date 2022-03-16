# from pudb import set_trace; set_trace()
from typing import List, Tuple


class Solution:
    def solveEquation(self, equation: str) -> str:
        """Split the equation into left and right half. For each half, obtain
        the total coefficient on x and total constant. Pay attention to the
        situation of "x" and "-x". They must be analyzed separately.

        O(N), 32 ms, 85% ranking.
        """
        left, right = equation.split('=')

        def get_coeff_const(exp: str) -> Tuple[int, int]:
            tokens = exp.replace('-', '+-').split('+')
            coeff, const = 0, 0
            for t in tokens:
                if t:
                    if t[-1] == 'x':
                        # careful about different coefficient situations
                        if len(t) == 1:
                            coeff += 1
                        elif len(t) == 2 and t[0] == '-':
                            coeff -= 1
                        else:
                            coeff += int(t[:-1])
                    else:
                        const += int(t)
            return coeff, const
        
        lcoeff, lconst = get_coeff_const(left)
        rcoeff, rconst = get_coeff_const(right)
        if lcoeff != rcoeff:
            return f'x={(rconst - lconst) // (lcoeff - rcoeff)}'
        return 'No solution' if lconst != rconst else 'Infinite solutions'


sol = Solution()
tests = [
    ("x+5-3+x=6+x-2", 'x=2'),
    ('x=x', 'Infinite solutions'),
    ('2x=x', 'x=0'),
    ('-x=-1', 'x=1'),
    ('-2x=-8', 'x=4'),
]

for i, (equation, ans) in enumerate(tests):
    res = sol.solveEquation(equation)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
