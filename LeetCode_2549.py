# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def distinctIntegers(self, n: int) -> int:
        """This feels wrong. It does pass, but I feel like there should be a
        math solution.

        O(N^2), 50 ms, faster than 18.97%
        """
        queue = [n]
        seen = set([n])
        res = 0
        while queue:
            res += len(queue)
            tmp = []
            for x in queue:
                for i in range(2, x):
                    if x % i == 1 and i not in seen:
                        tmp.append(i)
                        seen.add(i)
            queue = tmp
        return res


class Solution2:
    def distinctIntegers(self, n: int) -> int:
        """For n, n - 1 is its co-prime. For n - 1, n - 2 is its co-prime. Thus
        we can put all the numbers in range (1, n] on the board. Thus the result
        must be n - 1.

        O(1), 35 ms, faster than 54.28%
        """
        return n - 1 if n > 1 else 1



sol = Solution2()
tests = [
    (5, 4),
    (3, 2),
    (1, 1),
]

for i, (n, ans) in enumerate(tests):
    res = sol.distinctIntegers(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
